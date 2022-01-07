from django.db import models
from django.urls import reverse

class Driver(models.Model):
    id = models.IntegerField(max_length=20, unique=True)
    first_name = models.CharField(max_length=250)
    second_name = models.CharField(max_length=250)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class Vehicle(models.Model):
    id = models.IntegerField(max_length=20, unique=True)
    make = models.CharField(max_length=250)
    model = models.CharField(max_length=250)
    plate_number = models.CharField(max_length=250) # "AA 1234 OO"
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)






