"""Usser forms."""

#Django
from django import forms

#Model
from django.contrib.auth.models import User
from users.models import Profile

class SignupForm(forms.Form):
    """Signup Form"""
    username=forms.CharField(min_length=4,max_length=50)
    password=forms.CharField(max_length=70,widget=forms.PasswordInput())#para añadir un widget
    password_confirmation=forms.CharField(max_length=70,widget=forms.PasswordInput())
    first_name=forms.CharField(min_length=2,max_length=50)
    last_name=forms.CharField(min_length=2,max_length=50)
    email=forms.CharField(min_length=6,max_length=70,widget=forms.EmailInput())#usando otro widget

    def clean_username(self):#Validacion para usuario que sea unico DOCUMENTACION!!!
        """Username must be unique"""
        username=self.cleaned_data['username']#django ya limpia el valor y accedemos con cleaned_data
        username_taken=User.objects.filter(username=username).exists()#exist para que sea un booleano
        if username_taken:
            raise forms.ValidationError('Username is already in use.')   
        return username
    
    def clean(self):
        """Verify password confirmation match."""
        data=super().clean()#trae los datos sobreescritos

        password=data['password']
        password_confirmation=data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')
        return data

    def save(self):#se sobreescribe la funcion save
        """Create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirmation')#saca el dato que no es necesario guardar
        user=User.objects.create_user(**data)#con **data se manda todo el diccionario completo
        profile=Profile(user=user)
        profile.save()
        
class ProfileForm(forms.Form):
    """Profile form."""
    website=forms.URLField(max_length=200,required=True)
    biography=forms.CharField(max_length=500,required=False)
    phone_number=forms.CharField(max_length=20,required=False)
    picture=forms.ImageField()