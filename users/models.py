""" imports from django"""

from django.contrib.auth.models import User
from django.db import models


# Create your models here.

"""La clase extiende de la clase abstracta AppConfig"""
class Profile(models.Model):

    """Profile model

    Proxy mode that extends the base data other info"""

    """ Se manda por parametro el usuario como tal,
    y a manera en la que se elimina en la base de datos, el usuario y
    la clase de la que extiende """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)

    phone_number = models.CharField(max_length=20, blank=True)

    picture = models.ImageField(upload_to= 'users/pictures', blank = True, null= True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


  
        
    