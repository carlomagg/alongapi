from django.db import models

# Create your models here.

class Driver(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=10)
    state_of_residence =models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    vehicle_model = models.CharField(max_length=100)
    vehicle_year = models.CharField(max_length=100)
    plate_number = models.CharField(max_length=100)
    vehicle_color = models.CharField(max_length=100)
    driver_license = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

