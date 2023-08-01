from django.db import models
from django.db.models.deletion import CASCADE

class recruit(models.Model):
    studentname = models.CharField(max_length=100)
    studentaddess= models.CharField(max_length=1000,default="description")
    studentlocation= models.CharField(max_length=1000,default="description")
    def __str__(self):
        return self.name
    



class recruit_user_master(models.Model):
    usernamename = models.CharField(max_length=100)
    useraddressaddess= models.CharField(max_length=1000,default="description")
    userlocationlocation= models.CharField(max_length=1000,default="description")
    def __str__(self):
        return self.name    