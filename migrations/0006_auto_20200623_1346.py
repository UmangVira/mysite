# Generated by Django 2.1.5 on 2020-06-23 08:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200623_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 23, 13, 46, 20, 10322), verbose_name='Item updated'),
        ),
        migrations.AlterField(
            model_name='tender',
            name='tender_description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='tender',
            name='tender_updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 23, 13, 46, 20, 10322), verbose_name='Tender Updated'),
        ),
    ]