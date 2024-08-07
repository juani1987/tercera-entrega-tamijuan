from django import forms
from misdatos.moduls import*  
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserChangeForm


#class ClienteForm(forms.Form):
   # first_name = forms.CharField(max_length=50, required=True)
    #last_name = forms.CharField(max_length=50, required=True)
    #email = forms.EmailField(label="Email", required=False)
   # Opciones = (
       # (1, "Dejanos Tu Comntario y Ganate un Cafe"),
       # (2, "Hacer Sugerencias"),
        #(3, "Reclamos"),
   # )
   # show = forms.ChoiceField(label="Subs", choices=Opciones, required=True)
    #aplicado = forms.BooleanField()
    
class ClienteForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(required=True)   
    profesion = forms.CharField(max_length=50, required=True)

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Contraseña a confirmar", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
   
class UserEditForm (UserChangeForm):
   email = forms.EmailField(required=True)
   nombre = forms.CharField(label="Nombre", max_length=50, required=True)
   apellido = forms.CharField(label="Nombre", max_length=50, required=True)
 
class Meta:
    model = User
    fields =["email","first_name","last_name"]

class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)
