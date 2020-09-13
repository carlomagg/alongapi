from django.db import models

# Create your models here.

class Bookrides(models.Model):
    phone = models.CharField(max_length=11)
    pick_up = models.CharField(max_length=100)
    destination = models.CharField(max_length=100, unique=True)
   
    