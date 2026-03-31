from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    ROLE_CHOICES = [
        ('aluno', 'Aluno'),
        ('professor', 'Professor'),
        ('admin', 'Administrador'),
    ]

    NIVEL_CHOICES = [
        ('graduacao', 'Graduação'),
        ('latosensu', 'Lato Sensu'),
        ('mestrado', 'Mestrado'),
        ('doutorado', 'Doutorado'),
    ]

    matricula = models.CharField(max_length=20, unique=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField(null=True, blank=False)
    usuario = models.CharField(max_length=150, unique=True)

    role=models.CharField(max_length=20, choices=ROLE_CHOICES, blank=False)
    nivel=models.CharField(max_length=20, choices=NIVEL_CHOICES, blank=False)