from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    create_date = models.DateTimeField(auto_now_add=True)

class Group(models.Model):
    group_name  = models.CharField(max_length=20)
    create_date = models.DateTimeField(auto_now_add=True)
    members = models.ManyToManyField(User,through='Membership',through_fields=('group','user'),)

class Membership(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
