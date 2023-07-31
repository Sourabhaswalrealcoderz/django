# Create your models here.

  

from django.db import models
from django.db.models.deletion import CASCADE

class skill(models.Model):
    skillname = models.CharField(max_length=100)
    skilltype = models.CharField(max_length=100,default="new") 
    skillcategory = models.CharField(max_length=100,default="new")
    skillsubcategory = models.CharField(max_length=100,default="new")
    skillmincategory = models.CharField(max_length=100,default="new")
    newskill = models.CharField(max_length=100,default="new")
    skilladdess= models.CharField(max_length=1000,default="description")
    def __str__(self):
        return self.name
# Create your models here.
