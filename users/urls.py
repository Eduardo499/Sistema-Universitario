from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('users/', users, name='users_home'),
    path('gerenciar-alunos/', gerenciar_alunos, name='gerenciar_alunos'),

]