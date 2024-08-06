from django import forms
from misdatos.moduls import*  
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from misdatos.moduls import CustomUser


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
    
class UserRegisterForm(UserCreationForm):

    usuario = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
   
    nombre = forms.CharField()
    apellido = forms.CharField()
    imagen_avatar = forms.ImageField(required=False)
 
    class Meta:
                model = CustomUser
                fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name'] 
        #Saca los mensajes de ayuda
                help_texts = {k:"" for k in fields}

class UserEditForm(UserCreationForm):

    #Acá se definen las opciones que queres modificar del usuario, 
    #Ponemos las básicas
    email = forms.EmailField(label="Modificar E-mail")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 

    class Meta:
        model = User 
        fields = [ 'email', 'password1', 'password2'] 
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}

   

 
    
