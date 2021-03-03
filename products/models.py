from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField()
    description = models.TextField()

    @property
    def amount(self):
        return self.inventory.amount
