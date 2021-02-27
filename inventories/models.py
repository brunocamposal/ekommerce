from django.db import models

class Inventory(models.Model):
    amount = models.IntegerField()
    transaction_time = models.DateTimeField(null=True)
    transaction_type = models.CharField(max_length=128)

    