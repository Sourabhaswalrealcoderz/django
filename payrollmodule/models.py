from django.db import models
from django.db.models.deletion import CASCADE

class payrollapp(models.Model):
    payrollname = models.CharField(max_length=100)
    payrolladdess= models.CharField(max_length=1000,default="description")
    payrollocation= models.CharField(max_length=1000,default="description")


    def __str__(self):
        return self.name