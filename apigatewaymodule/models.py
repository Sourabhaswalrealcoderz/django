from django.db import models
from django.db.models.deletion import CASCADE

class apigatewayapp(models.Model):
    apigatewayname = models.CharField(max_length=100)
    apigatewayaddess= models.CharField(max_length=1000,default="description")
    apigatewaylocation= models.CharField(max_length=1000,default="description")


    def __str__(self):
        return self.name