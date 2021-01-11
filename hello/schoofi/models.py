from django.db import models

# Create your models here.


class user(models.Model):
    Name=models.CharField(max_length=150)
    School=models.CharField(max_length=150)
    Rollno=models.CharField(max_length=150)
    Email=models.CharField(max_length=150)
    Password=models.CharField(max_length=150)
    Confirmpassword=models.CharField(max_length=150)
    





    
