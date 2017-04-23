# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 19:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviefinder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='awards',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='box_office',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='content_type',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='country',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='dvd',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdb_id',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdb_rating',
            field=models.FloatField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdb_votes',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='metascore',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='plot',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='production',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name='movie',
            name='ratings',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='released',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='runtime',
            field=models.DurationField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='website',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='writer',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.PositiveSmallIntegerField(blank=True),
        ),
    ]