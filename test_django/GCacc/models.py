from django.db import models

# Create your models here.

class User(models.Model):
    username = models.Char(max_lenght=30)
    password = models.Char(max_lenght=10)
    create_date = models.DateTimeField()

class Group():
    group_name  = models.Char(max_lenght=30)
    
