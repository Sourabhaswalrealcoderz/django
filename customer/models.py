# Create your models here.


from django.db import models
from django.db.models.deletion import CASCADE

class customer(models.Model):
    name = models.CharField(max_length=100)
    addess= models.CharField(max_length=1000,default="description")
    location= models.CharField(max_length=1000,default="description")
    def __str__(self):
        return self.name



class seller(models.Model):
    sellername = models.CharField(max_length=100)
   selleraddess= models.CharField(max_length=1000,default="description")
    sellerlocation= models.CharField(max_length=1000,default="description")
    def __str__(self):
        return self.name
