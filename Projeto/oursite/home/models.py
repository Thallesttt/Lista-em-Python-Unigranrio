from django.db import models

# Create your models here.
class Home_Model(models.Model):
        Name = models.CharField(Max_length = 50)
        Senha = models.CharFiled(Max_length = 20)
        LastName=models.CharField(Max_length= 100)



       
