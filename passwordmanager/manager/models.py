from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

class  Passwords(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Passwords"
