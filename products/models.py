from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField()
    description = models.TextField()

    @property
    def amount(self):
        return self.inventory.amount

    @property
    def inventory_id(self):
        return self.inventory.id
