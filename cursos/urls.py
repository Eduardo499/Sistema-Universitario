from django.urls import path
from .views import *

app_name = 'cursos'

urlpatterns = [
    path('cursos/', cursos, name='cursos_home'),
]