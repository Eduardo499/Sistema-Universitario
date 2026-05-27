from django.shortcuts import render

# Create your views here.
def users(request):
    return render(request, 'users/users_home.html')

def gerenciar_alunos(request):
    return render(request, 'users/gerenciar_alunos.html')