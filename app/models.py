from django.db import models

# Create your models here.
class EmployeeModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50,unique=True)
    contact = models.IntegerField(unique=True)
    password = models.CharField(max_length=30)