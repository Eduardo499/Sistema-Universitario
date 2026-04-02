from django.urls import path
from .views import *

app_name = 'cursos'

urlpatterns = [
    path('cursos/', cursos, name='cursos_home'),
    path('cursos/gerenciar/', gerenciar_cursos, name='gerenciar_cursos'),
    path('cursos/gerenciar/adicionar/', adicionar_curso, name='adicionar_curso'),
    path('cursos/gerenciar/editar/<int:curso_id>/', editar_curso, name='editar_curso'),
    path('cursos/gerenciar/excluir/<int:curso_id>/', excluir_curso, name='excluir_curso'),
]