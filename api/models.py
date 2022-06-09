from operator import mod
from django.db import models

# Create your models here.

class registration(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    Roll_number = models.IntegerField()
    address = models.TextField()
    gender = models.CharField(max_length=10)
