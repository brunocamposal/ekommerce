from django.db.models.fields import BooleanField
from products.models import Product
from django.db import models


class Inventory(models.Model):
    available = BooleanField(default=False)
    transaction_type = models.CharField(max_length=50)
    amount = models.IntegerField()
    transaction_time = models.DateTimeField(null=True)
    product_id = models.OneToOneField(Product, on_delete=models.CASCADE)

    def available_product(self):
        if self.amount > 0:
            self.available = True
        else:
            self.available = False
