from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
