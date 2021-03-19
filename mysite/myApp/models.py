from django.db import models


# Create your models here.

class User(models.Model):
    uid = models.CharField(max_length=20)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=15)
    password = models.CharField(max_length=20)

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    message = models.CharField(max_length=500)
