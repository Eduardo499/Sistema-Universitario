from django import forms
from .models import Curso, Disciplina

class CustomForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = [
            'nome',
            'grau',
            'qtd_semestres',
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['grau'].choices = [
            choice for choice in self.fields['grau'].choices if choice[0] != ''
        ]

class CursoChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.nome} ({obj.get_grau_display()})"

class CustomDisciplinaForm(forms.ModelForm):
    curso = CursoChoiceField(queryset=Curso.objects.all())
    class Meta:
        model = Disciplina
        fields = [
            'nome',
            'curso',
        ]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['curso'].choices = [
            choice for choice in self.fields['curso'].choices if choice[0] != ''
        ]

    def clean(self):
        cleaned_data = super().clean()
        nome = cleaned_data.get('nome')
        curso = cleaned_data.get('curso')

        if Disciplina.objects.filter(nome=nome, curso=curso).exists():
            raise forms.ValidationError("Já existe uma disciplina com esse nome para o curso selecionado.")
        return cleaned_data