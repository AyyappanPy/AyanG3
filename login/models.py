from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Login(models.Model):

    username = models.CharField(max_length=25)
    password = models.CharField(max_length=10)

class SignIn(models.Model):

    username = models.CharField(max_length=25)
    password = models.CharField(max_length=10)
    repeat_password = models.CharField(max_length=10)