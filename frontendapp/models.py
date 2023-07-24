from django.db import models


# Create your models here.

class cartdb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Quantity = models.IntegerField(null=True, blank=True)
    Total = models.IntegerField(null=True, blank=True)


class cartaddress(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=500, null=True, blank=True)
    State = models.CharField(max_length=100, null=True, blank=True)
    Zip = models.CharField(max_length=100, null=True, blank=True)
    Mail = models.EmailField(max_length=100, null=True, blank=True)
    Num = models.IntegerField(null=True, blank=True)


class customerdetails(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Mail = models.EmailField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)
    Confirm = models.CharField(max_length=100, null=True, blank=True)
