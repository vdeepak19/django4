from django.db import models

# Create your models here.
class register(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=100)
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=100, primary_key=True)
    class Meta:
         db_table="register"

