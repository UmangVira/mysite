# Generated by Django 2.1.5 on 2020-07-01 16:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20200701_2205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estimate',
            name='est_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.TenderEstimate', verbose_name='Estimate Number'),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 22, 5, 57, 111993), verbose_name='Item updated'),
        ),
        migrations.AlterField(
            model_name='tender',
            name='tender_updated',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 1, 22, 5, 57, 112994), verbose_name='Tender Updated'),
        ),
    ]
