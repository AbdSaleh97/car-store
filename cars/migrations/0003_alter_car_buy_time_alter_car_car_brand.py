# Generated by Django 5.0.7 on 2024-07-22 10:18

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_car_buy_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='buy_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_brand',
            field=models.CharField(max_length=200),
        ),
    ]
