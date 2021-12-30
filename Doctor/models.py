from django.db import models
from django.contrib.auth import get_user_model


class Doctor(models.Model):
<<<<<<< HEAD
    name = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True, max_length=30, verbose_name="Email Address")
    phone_number = models.CharField(unique=True, max_length=14,null=True,blank=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    town = models.CharField(max_length=20, blank=True, null=True)
    building_number = models.CharField(max_length=20, blank=True, null=True)
    street = models.CharField(max_length=20, blank=True, null=True)
    user = models.ForeignKey(get_user_model() , on_delete = models.CASCADE) 

    
=======


    gender_category=(
        ('Male','Male'),
        ('Female','Female'),
    )

    category=(
        ('Anesthesiology','Anesthesiology'),
        ('Neurology','Neurology'),
        ('Pathology','Pathology'),
        ('Surgery','Surgery'),
    )

    name = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(unique=True, max_length=20, verbose_name="Email Address")
    phone_number = models.CharField(unique=True, max_length=14,null=True,blank=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    gender=models.CharField(max_length=100,null=True,choices=gender_category)

    specialty=models.CharField(max_length=100,null=True,choices=category)
    town = models.CharField(max_length=20, blank=True, null=True)
    building_number = models.CharField(max_length=20, blank=True, null=True)
    street = models.CharField(max_length=20, blank=True, null=True)
>>>>>>> 7ba62cfdc11daecef80eb3625d30697bed52bfce



    def __str__(self):
<<<<<<< HEAD
        return self.name
=======
        return self.name

>>>>>>> 7ba62cfdc11daecef80eb3625d30697bed52bfce
