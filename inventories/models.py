from django.db.models import indexes
from django.db.models.fields import BooleanField
from products.models import Product
from django.db import models
from django.contrib.auth.models import User


class Inventory(models.Model):
    available = BooleanField(default=False)
    total_amount = models.IntegerField()
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


    def available_product(self):
        if self.total_amount > 0:
            self.available = True
        else:
            self.available = False

    @property
    def product_data(self):
        return self._product_data

    @product_data.setter
    def product_data(self, product):
        self._product_data = product

    

class InventoryRecords(models.Model):
    amount = models.IntegerField()
    transaction_type = models.CharField(max_length=50)
    transaction_time = models.DateTimeField(null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    seller = models.ForeignKey(User, on_delete=models.CASCADE)

    @property
    def product_data(self):
        return self._product_data

    @product_data.setter
    def product_data(self, product):
        self._product_data = product

    class Meta:
        indexes = [
            models.Index(fields=['seller', 'transaction_type' ])
        ]