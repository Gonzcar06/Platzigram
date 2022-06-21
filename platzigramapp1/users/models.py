'''User Models'''
#Django
from distutils.command.upload import upload
from operator import mod
from pyexpat import model
from django.contrib.auth.models import User##trae user del que ya esta creado por django
from django.db import models

class Profile(models.Model):
    """Profile model.
    
    Proxy model that extends the base data with other information.
    """
    user =models.OneToOneField(User,on_delete=models.CASCADE)#solo puede haber un usuario por modelos
    website=models.URLField(max_length=200, blank=True)
    biography=models.TextField(blank=True)
    phone_number=models.CharField(max_length=20,blank=True)

    picture=models.ImageField(
        upload_to='user/picture',
        blank=True,
        null=True
    )
    # instalar pip install pillow para poder usar imagenes

    created=models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username."""
        return self.user.username