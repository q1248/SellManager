import null as null
from django.db import models


# Create your models here.
class someTips(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=300)
    group = models.CharField(max_length=100)


class tickets(models.Model):
    name = models.CharField(max_length=100, unique=True)
    startStation = models.CharField(max_length=100)
    endStation = models.CharField(max_length=100)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    totalTime = models.CharField(max_length=100)
    type = models.CharField(max_length=30)
    backkups = models.CharField(max_length=100)
