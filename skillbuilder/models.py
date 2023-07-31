

from django.db import models




from django.db.models.deletion import CASCADE













class employee(models.Model):




    name = models.CharField(max_length=100)




    addess= models.CharField(max_length=1000,default="description")







    def __str__(self):




        return self.name
# Create your models here.
