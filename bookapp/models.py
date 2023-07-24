from django.db import models


# Create your models here.

class categorydb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)
    Descript = models.CharField(max_length=100, null=True, blank=True)


class productdb(models.Model):
    Bname = models.CharField(max_length=100, null=True, blank=True)
    Aname = models.CharField(max_length=100, null=True, blank=True)
    Category = models.CharField(max_length=100, null=True, blank=True)
    Image = models.ImageField(upload_to="profile", null=True, blank=True)
    Lang = models.CharField(max_length=100, null=True, blank=True)
    Descript = models.CharField(max_length=100, null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
