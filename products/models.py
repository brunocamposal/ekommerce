from django.db import models
from inventories.models import Inventory

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField()
    description = models.TextField()
    inventory = models.OneToOneField(Inventory, on_delete=models.CASCADE, related_name='inventory amount')

    @property
    def amount(self):
        return self.inventory.amount
