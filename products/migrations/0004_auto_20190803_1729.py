# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-08-03 17:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20190803_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='history',
            field=models.CharField(max_length=1000),
        ),
    ]
