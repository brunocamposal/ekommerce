# Generated by Django 3.1.7 on 2021-02-28 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('transaction_time', models.DateTimeField(null=True)),
                ('transaction_type', models.CharField(max_length=50)),
            ],
        ),
    ]
