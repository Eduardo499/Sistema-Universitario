from django.shortcuts import render, redirect
from .forms import *
from .models import *
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from django.http import HttpResponse
from itertools import groupby


# Create your views here.
def cursos(request):
    return render(request, 'cursos/cursos_home.html')

def gerenciar_cursos(request):
    cursos = Curso.objects.all()
    return render(request, 'cursos/gerenciar_cursos.html', {'cursos': cursos})

def adicionar_curso(request):
    if request.method == 'POST':
        form = CustomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cursos:gerenciar_cursos')
    else:
        form = CustomForm()
    return render(request, 'cursos/adicionar_curso.html', {'form': form})

def editar_curso(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    if request.method == 'POST':
        form = CustomForm(request.POST, instance=curso)
        if form.is_valid():
            form.save()
            return redirect('cursos:gerenciar_cursos')
    else:
        form = CustomForm(instance=curso)
    return render(request, 'cursos/adicionar_curso.html', {'form': form, 'curso': curso})

def excluir_curso(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    if request.method == 'POST':
        curso.delete()
        return redirect('cursos:gerenciar_cursos')
    return render(request, 'cursos/gerenciar_cursos.html', {'curso': curso})

def info_curso(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    return render(request, 'cursos/info_curso.html', {'curso': curso})

def gerenciar_disciplinas(request):
    disciplinas = Disciplina.objects.all()
    return render(request, 'cursos/gerenciar_disciplinas.html', {'disciplinas': disciplinas})

def adicionar_disciplina(request):
    if request.method == 'POST':
        form = CustomDisciplinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cursos:gerenciar_disciplinas')
    else:
        form = CustomDisciplinaForm()
    return render(request, 'cursos/adicionar_disciplina.html', {'form': form})

def excluir_disciplina(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)
    if request.method == 'POST':
        disciplina.delete()
        return redirect('cursos:gerenciar_disciplinas')
    return render(request, 'cursos/gerenciar_disciplinas.html', {'disciplina': disciplina})

def editar_disciplina(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)
    if request.method == 'POST':
        form = CustomDisciplinaForm(request.POST, instance=disciplina)
        if form.is_valid():
            form.save()
            return redirect('cursos:gerenciar_disciplinas')
    else:
        form = CustomDisciplinaForm(instance=disciplina)
    return render(request, 'cursos/adicionar_disciplina.html', {'form': form, 'disciplina': disciplina})

def info_disciplina(request, disciplina_id):
    disciplina = Disciplina.objects.get(id=disciplina_id)
    return render(request, 'cursos/info_disciplina.html', {'disciplina': disciplina})

def gerenciar_grade_curricular(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    grade_curricular = GradeCurricular.objects.filter(curso=curso).order_by('semestre')
    disciplinas_na_grade = list(grade_curricular.values_list('disciplina_id', flat=True))
    disciplinas_disponiveis = Disciplina.objects.filter(curso=curso).exclude(id__in=disciplinas_na_grade)

    erro = None

    if request.method == 'POST':
        disciplina_id = request.POST.get('disciplina')
        semestre = request.POST.get('semestre')

        if disciplina_id and semestre:
            disciplina = Disciplina.objects.get(id=disciplina_id)
            ja_existe = GradeCurricular.objects.filter(curso=curso, disciplina=disciplina).exists()  # sem semestre
            if ja_existe:
                erro = f'A disciplina "{disciplina.nome}" já está na grade curricular.'
            else:
                GradeCurricular.objects.create(curso=curso, disciplina=disciplina, semestre=semestre)
                return redirect('cursos:gerenciar_grade_curricular', curso_id=curso.id)

    return render(request, 'cursos/gerenciar_grade_curricular.html', {
        'curso': curso,
        'disciplinas': disciplinas_disponiveis,  # só as disponíveis
        'grade_curricular': grade_curricular,
        'semestres': range(1, curso.qtd_semestres + 1),
        'erro': erro
    })

def remover_grade_curricular(request,grade_id):
    grade = GradeCurricular.objects.get(id=grade_id)
    curso_id = grade.curso.id
    grade.delete()
    return redirect('cursos:gerenciar_grade_curricular', curso_id=curso_id)

def baixar_grade_curricular(request, curso_id):
    curso = Curso.objects.get(id=curso_id)
    grade_curricular = GradeCurricular.objects.filter(curso=curso).order_by('semestre')

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename="grade_curricular_{curso.nome}.pdf"'

    doc = SimpleDocTemplate(response, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    title = Paragraph(f"Grade Curricular - {curso.nome} ({curso.get_grau_display()})", styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 12))

    data = [['Semestre', 'Disciplina']]
    for semestre, disciplinas in groupby(grade_curricular, key=lambda x: x.semestre):
        for grade in disciplinas:
            data.append([f'Semestre {semestre}', grade.disciplina.nome])

    table = Table(data, colWidths=[100, 400])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1e293b')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#2d1515')),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.white),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#444444')),
    ]))
    elements.append(table)

    doc.build(elements)
    return response