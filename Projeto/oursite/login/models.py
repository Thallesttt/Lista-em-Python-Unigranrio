from django.db import models

# Create your models here.
class User(models.Model):
    Nome=models.CharField(max_length=150)
    Data_Registro = models.DateTimeField()
   
 