# Generated by Django 3.1.7 on 2021-03-04 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.FloatField()),
                ('status', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('client_id', models.IntegerField()),
                ('product_list', models.ManyToManyField(related_name='orders', to='products.Product')),
            ],
        ),
    ]
