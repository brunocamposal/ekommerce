from django.db import models
from products.models import Product


class Order(models.Model):
    total_price = models.FloatField()
    status = models.CharField(max_length=255)
    comments = models.CharField(max_length=255)
    product_list = models.ManyToManyField(
        Product, related_name='orders')
    client_id = models.IntegerField()

