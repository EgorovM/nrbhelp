# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-10 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('help', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='telephone',
            field=models.CharField(max_length=10),
        ),
    ]
