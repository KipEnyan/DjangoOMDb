# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-19 07:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviefinder', '0009_auto_20170419_0303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='Year',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
