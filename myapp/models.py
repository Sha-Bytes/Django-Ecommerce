from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class contact(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=100)
    email = models.EmailField()
    Phone_no = models.CharField(max_length=100)
    Message = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Order(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    house_no = models.CharField(max_length=100)
    street = models.CharField(max_length=200)
    landmark = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    date = models.DateField(default=datetime.datetime.today)
    def __str__(self):
        return self.product

