from django.db import models

class Inventory(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.CharField(max_length=250)
    category = models.CharField(max_length=50)
    amount = models.IntegerField()