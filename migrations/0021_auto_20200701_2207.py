# Generated by Django 2.1.5 on 2020-07-01 16:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20200701_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 22, 7, 25, 22551), verbose_name='Item updated'),
        ),
        migrations.AlterField(
            model_name='tender',
            name='tender_updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 22, 7, 25, 23551), verbose_name='Tender Updated'),
        ),
    ]
