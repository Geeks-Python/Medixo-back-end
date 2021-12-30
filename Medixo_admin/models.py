from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_admin= models.BooleanField('Is admin', default=False)
    is_customer = models.BooleanField('Is customer', default=False)
    is_employee = models.BooleanField('Is employee', default=False)


class Customer(models.Model):
    email = models.EmailField(unique=True, max_length=20, verbose_name="Email Address")
    country = models.CharField(max_length=20, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    


    def __str__(self) -> str:
        return self.email

    
class Pharmacy(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True, max_length=20, verbose_name="Email Address")
    phone_number = models.CharField(unique=True, max_length=14,null=True,blank=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    town = models.CharField(max_length=20, blank=True, null=True)
    building_number = models.CharField(max_length=20, blank=True, null=True)
    street = models.CharField(max_length=20, blank=True, null=True)
    
    def __str__(self):
        return self.name

