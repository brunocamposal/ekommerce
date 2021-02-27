from django.db import models


class Order(models.Model):
    total_price = models.FloatField()
    status = models.CharField(max_length=255)
    description = models.CarField(max_length=255)
    product_list = models.ManyToManyField(Product, related_name='orders')
    client_id = models.IntegerField()
    #  models.ForeignKey(User, on_delete=models.CASCADE)
