from django.db import models
from django.db.models.deletion import CASCADE

class engageapp(models.Model):
    managename = models.CharField(max_length=100)
    manageaddess= models.CharField(max_length=1000,default="description")
    managelocation= models.CharField(max_length=1000,default="description")



class engage_performqance_app(models.Model):
    managename = models.CharField(max_length=100)
    manageaddess= models.CharField(max_length=1000,default="description")
    managelocation= models.CharField(max_length=1000,default="description") 



class engage_gcp(models.Model):
    managename = models.CharField(max_length=100)
    manageaddess= models.CharField(max_length=1000,default="description")
    managelocation= models.CharField(max_length=1000,default="description") 


    def __str__(self):
        return self.name
