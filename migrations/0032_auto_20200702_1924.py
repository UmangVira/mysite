# Generated by Django 2.1.5 on 2020-07-02 13:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_auto_20200702_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 2, 19, 24, 14, 157871), verbose_name='Item updated'),
        ),
        migrations.AlterField(
            model_name='tender',
            name='tender_updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 2, 19, 24, 14, 158872), verbose_name='Tender Updated'),
        ),
    ]
