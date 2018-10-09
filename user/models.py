from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    birth_date = models.DateField()
    created_on = models.DateField()

class UserDetails(models.Model):
    phone_number = models.CharField(max_length=100)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    address = models.CharField(max_length=150)
    pin = models.CharField(max_length=10)
