# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-13 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20170411_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dreamreal',
            name='date',
            field=models.DateField(max_length=50),
        ),
    ]
