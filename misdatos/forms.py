from django import forms
from misdatos.moduls import*  
from django.contrib.auth.models import AbstractUser


class ClienteForm(forms.Form):
    first_name = forms.CharField(max_length=50, required=True)
    last_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(label="Email", required=False)
    Opciones = (
        (1, "Dejanos Tu Comntario y Ganate un Cafe"),
        (2, "Hacer Sugerencias"),
        (3, "Reclamos"),
    )
    show = forms.ChoiceField(label="Subs", choices=Opciones, required=True)
    aplicado = forms.BooleanField()
    
class CustomUser(AbstractUser):
    username = models.CharField('nombre de usuario', unique=True, max_length=150)
    password = models.CharField('password',unique=True, max_length=150)

# En tu formulario de registro
class RegisterForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', ...]

    
    
