from django.db import models
from django.contrib.auth import get_user_model


class Doctor(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True, max_length=30, verbose_name="Email Address")
    phone_number = models.CharField(unique=True, max_length=14,null=True,blank=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    town = models.CharField(max_length=20, blank=True, null=True)
    building_number = models.CharField(max_length=20, blank=True, null=True)
    street = models.CharField(max_length=20, blank=True, null=True)
    user = models.ForeignKey(get_user_model() , on_delete = models.CASCADE) 

    



    def __str__(self):
        return self.name