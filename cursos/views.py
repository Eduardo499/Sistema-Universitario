from django.shortcuts import render, redirect
from .forms import CustomForm
from .models import Curso

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