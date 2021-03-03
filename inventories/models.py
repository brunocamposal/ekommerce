from django.db.models.fields import BooleanField
from products.models import Product
from django.db import models


class Inventory(models.Model):
    available = BooleanField(default=False)
    total_amount = models.IntegerField()
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    def available_product(self):
        if self.total_amount > 0:
            self.available = True
        else:
            self.available = False


class InventoryRecords(models.Model):
    amount = models.IntegerField()
    transaction_type = models.CharField(max_length=50)
    transaction_time = models.DateTimeField(null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
