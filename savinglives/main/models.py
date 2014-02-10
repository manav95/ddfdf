from django.db import models

class Operation(models.Model):
    name =  models.CharField(max_length=128, unique=True)
    url = models.URLField()
class SendText(models.Model):
    phoneNumber = models.CharField(max_length=128, unique=True)
    message = models.CharField(max_length=128, unique=True)
class SendCall(models.Model):
     phoneNumber = models.CharField(max_length=128, unique=True)
class LookUpNearestWorker(models.Model):
     xLocation = models.IntegerField(default=0, unique=True)
     yLocation = models.IntegerField(default=0, unique=True)
class EnterNewWorker(models.Model):
     phoneNumber = models.CharField(max_length=128, unique=True)
     name = models.CharField(max_length=128, unique=True)
     xLocation = models.IntegerField(default=0, unique=True)
     yLocation = models.IntegerField(default=0, unique=True)
     
