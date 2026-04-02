from django.db import models

# Create your models here.
class Curso(models.Model):
    GRAU_CHOICES = [
        ('bacharelado', 'Bacharelado'),
        ('licenciatura', 'Licenciatura'),
        ('tecnologo', 'Tecnólogo')
    ]

    nome = models.CharField(max_length=100)
    grau = models.CharField(max_length=50, choices=GRAU_CHOICES)
    qtd_semestres = models.IntegerField()

    class Meta:
        unique_together = ('nome', 'grau')
    
    def __str__(self):
        return self.nome