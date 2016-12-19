from __future__ import unicode_literals

from django.db import models

# Create your models here.

class EditProfile(models.Model):

    name = models.CharField(max_length=25)
    dob = models.DateField()
    pnoneno = models.CharField(max_length=25)
    address = models.TextField()
    email = models.EmailField(max_length=70,blank=True)
    website = models.CharField(max_length=70,blank=True)
