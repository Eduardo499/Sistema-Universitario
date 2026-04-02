from django.urls import path
from .views import *

app_name = 'cursos'

urlpatterns = [
    path('cursos/', cursos, name='cursos_home'),
    path('cursos/gerenciar/', gerenciar_cursos, name='gerenciar_cursos'),
    path('cursos/gerenciar/adicionar/', adicionar_curso, name='adicionar_curso'),
    path('cursos/gerenciar/editar/<int:curso_id>/', editar_curso, name='editar_curso'),
    path('cursos/gerenciar/excluir/<int:curso_id>/', excluir_curso, name='excluir_curso'),
    path('cursos/gerenciar/info/<int:curso_id>/', info_curso, name='info_curso'),
    path('cursos/disciplinas/', gerenciar_disciplinas, name='gerenciar_disciplinas'),
    path('cursos/disciplinas/adicionar/', adicionar_disciplina, name='adicionar_disciplina'),
    path('cursos/disciplinas/editar/<int:disciplina_id>/', editar_disciplina, name='editar_disciplina'),
    path('cursos/disciplinas/excluir/<int:disciplina_id>/', excluir_disciplina, name='excluir_disciplina'),
    path('cursos/disciplinas/info/<int:disciplina_id>/', info_disciplina, name='info_disciplina'),
    path('cursos/gerenciar_grade_curricular/<int:curso_id>/', gerenciar_grade_curricular, name='gerenciar_grade_curricular'),
    path('cursos/grade/remover/<int:grade_id>/', remover_grade_curricular, name='remover_grade_curricular'),
    path('cursos/baixar_grade/<int:curso_id>/', baixar_grade_curricular, name='baixar_grade_curricular'),

]