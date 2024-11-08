from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class Formulario_Registrarse(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_text = {key: "" for key in fields}

class Formulario_editar_perfil(UserChangeForm):
    first_name = forms.CharField(label="Usuario")
    email = forms.EmailField()
    password = None      
    class Meta:
        model = User
        fields = ["first_name", "email"]
        