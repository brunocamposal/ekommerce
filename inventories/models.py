from django.db import models
from products.models import Product

class Inventory(models.Model):
    amount = models.IntegerField()
    transaction_time = models.DateTimeField(null=True)
    transaction_type = models.CharField()

    product_id = models.ForeignKey(Product)