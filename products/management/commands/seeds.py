from django.core.management.base import BaseCommand
from products.models import Product
from inventories.models import Inventory

import csv

class Command(BaseCommand):
    help = 'Populate db from csv file'
    
    def add_arguments(self, parser):
        parser.add_argument('csvfile', type=str, help='path to .csv file')


    def handle(self, *args, **kwargs):
        print('starting')
        csvfile = kwargs['csvfile']
        with open(csvfile) as file:
           
           products = csv.DictReader(file)
           product_list = []
           inventory_list = []
               
               
            for product_data in products:
                product = Product(
                name=product_data['name'],
                price=productData['price'],
                description=product_data['description'],
                category=product_data['category'],
                image=product_data['image'],
                )

                inventory = Inventory(
                    total_amount=product_data['amount'],
                    product=product,
                )

                product_list.append(product)
                inventory_list.append(inventory)
        

            Product.objects.bulk_create(product_list,   batch_size=500)
            Inventory.objects.bulk_create(inventory_list, batch_size=500)
            print('finished')