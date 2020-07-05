# Generated by Django 2.1.5 on 2020-06-22 04:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200622_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_quantity',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='item_updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 22, 10, 12, 14, 319737), verbose_name='Item updated'),
        ),
    ]
