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
            'username',
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
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está em uso.")

        return email
    
    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Este nome de usuário já está em uso.")

        return username
    
    def clean_matricula(self):
        matricula = self.cleaned_data.get('matricula')

        if User.objects.filter(matricula=matricula).exists():
            raise forms.ValidationError("Esta matrícula já está em uso.")

        return matricula

    