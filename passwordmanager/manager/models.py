from django.db import models
from django.contrib.auth.models import User


class  Passwords(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=200)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Passwords"
