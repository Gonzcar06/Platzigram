from django.db import models

# Create your models here.
"""POSTS MODELS."""
from django.db import models
from django.contrib.auth.models import User


#class User(models.Model):
#    """user model."""
#    email= models.EmailField(unique=True)##para que solo exista un email
#    password= models.CharField(max_length=100)

#    first_name = models.CharField(max_length=100)
#    last_name = models.CharField(max_length=100)

#    is_admin=models.BooleanField(default=False)

#    bio = models.TextField()

#    birthdate = models.DateField(blank=True,null=True)#valor blanco no necesario

#    created = models.DateTimeField(auto_now_add=True)#cuando se cree una instancia le va a crear la fecha en la que se creo
#    modified = models.DateTimeField(auto_now=True)#crear la fecha en la que se edito la ultima vez


#    def __str__(self):
#        return self.email
    #python manage.py makemigrations cada vez que se modifica o se crea un modelo
    #python manage.py migrate para sacara los warning al momento de correr el servidor

class Post(models.Model):
    """Post model."""

    user = models.ForeignKey(User,on_delete=models.CASCADE)###LLAVE PARA RELACIONAR CON EL USUSARIO
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)
                                ###SE LLAMA ASI PARA NO ESTAR IMPORTANDO"###
    title = models.CharField(max_length=255)
    photo = models.ImageField(
        upload_to='posts/photos',
        blank=True,
        null=True,
    )
    created = models.DateField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return title and username."""
        return '{} by @{}'.format(self.title,self.user.username)