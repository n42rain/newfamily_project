from django.db import models

# Create your models here.

class Family(models.Model):
    name = models.TextField(max_length=100)
    age = models.IntegerField()
    icno = models.CharField(max_length=22,primary_key=True)
    work = models.TextField(max_length=100)


