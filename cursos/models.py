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
    
class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('nome', 'curso')

    def __str__(self):
        return self.nome
    
class GradeCurricular(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='grade')
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    semestre = models.IntegerField()

    class Meta:
        unique_together = ('curso', 'disciplina', 'semestre')

    def __str__(self):
        return f"{self.curso.nome} - {self.disciplina.nome} (Semestre {self.semestre})"
