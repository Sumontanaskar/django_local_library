# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dreamreal',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('host', models.CharField(max_length=50)),
                ('date', models.DateField(max_length=50)),
                ('Din', models.IntegerField()),
            ],
            options={
                'db_table': 'dreamreal',
            },
        ),
    ]