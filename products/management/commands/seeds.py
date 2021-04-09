from django.core.management.base import BaseCommand
from products.models import Product
from inventories.models import Inventory
from django.contrib.auth.models import User

import csv

class Command(BaseCommand):
    help = 'Populate db from csv file'
    
    def add_arguments(self, parser):
        parser.add_argument('csvfile', type=str, help='path to .csv file')

    def handle(self, *args, **kwargs):
        print('starting')
        user = User.objects.get(id=3)
        csvfile = kwargs['csvfile']
        with open(csvfile) as file:
           
            products = csv.DictReader(file)
            product_list = []
            inventory_list = []
        
               
            for product_data in products:
                product = Product.objects.create(
                name=product_data['name'],
                price=float(product_data['price'].replace(',', '.')),
                description=product_data['description'],
                category=product_data['category'],
                image=product_data['image'],
                )
              
                inventory = Inventory.objects.create(
                    total_amount=product_data['amount'],
                    product=product,
                    available=True,
                    seller=user
                )

                product_list.append(product)
                inventory_list.append(inventory)
        

           
            print('finished')