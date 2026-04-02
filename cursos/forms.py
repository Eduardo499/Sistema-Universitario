from django import forms
from .models import Curso

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
