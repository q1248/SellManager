from django.db import models


# Create your models here.
class someTips(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=300)
    group = models.CharField(max_length=100)
    aritcle = models.CharField(max_length=1000, default="This is some describe")


class tickets(models.Model):
    name = models.CharField(max_length=100, unique=True)
    startStation = models.CharField(max_length=100)
    endStation = models.CharField(max_length=100)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    totalTime = models.CharField(max_length=100)
    leftTicket = models.IntegerField(default=100)
    type = models.CharField(max_length=30)


class customer(models.Model):
    u_name = models.CharField(max_length=10)
    u_password = models.CharField(max_length=255)
    u_ticket = models.CharField(max_length=30, null=True)
    u_email = models.EmailField()


class PurchaseHistory(models.Model):
    customerName = models.CharField(max_length=10)
    ticketId = models.CharField(max_length=50, unique=True)
