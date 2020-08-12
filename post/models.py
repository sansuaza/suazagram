""" post models"""
from django.db import models


class user(models.Model):

    """ emaill unico en la base de datos """
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    bio = models.TextField(blank=True)

    """ El campo puede no estar diligenciado, y si no lo está 
    se pondrá el valor null """
    birthdate = models.DateField(blank=True, null = True)

    """ se le da la fecha de el dia en el que de crea """
    created = models.DateTimeField(auto_now_add=True)

    """ Se edita la fecha el dia en que se modifica por
    ultima vez"""
    modified = models.DateTimeField(auto_now=True)


# Create your models here.
