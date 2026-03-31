from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from datetime import date

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'nome',
            'email',
            'matricula',
            'data_nascimento',
            'usuario',
            'role',
            'nivel',
            'password1',
            'password2',
        ]

        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nivel'].choices = [
            choice for choice in self.fields['nivel'].choices if choice[0] != ''
        ]

        self.fields['role'].choices = [
            choice for choice in self.fields['role'].choices if choice[0] != ''
        ]

    def clean_data_nascimento(self):
        data = self.cleaned_data.get('data_nascimento')

        if data:
            hoje = date.today()

            if data > hoje:
                raise forms.ValidationError("Data inválida.")

        return data

    