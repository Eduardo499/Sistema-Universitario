from django.shortcuts import render, redirect
from .forms import *
from .models import *

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