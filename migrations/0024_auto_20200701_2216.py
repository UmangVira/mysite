# Generated by Django 2.1.5 on 2020-07-01 16:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_auto_20200701_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estimateitem',
            name='item_qty',
            field=models.CharField(max_length=20, verbose_name='Item Quantity Needed'),
        ),
        migrations.AlterField(
            model_name='estimateitem',
            name='qty_con',
            field=models.CharField(max_length=20, verbose_name='Quantity provided by contractor'),
        ),
        migrations.AlterField(
            model_name='estimateitem',
            name='qty_cus',
            field=models.CharField(max_length=20, verbose_name='Quantity provided by customer'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 22, 16, 27, 962945), verbose_name='Item updated'),
        ),
        migrations.AlterField(
            model_name='tender',
            name='tender_updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 22, 16, 27, 963944), verbose_name='Tender Updated'),
        ),
    ]
