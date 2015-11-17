# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('code', models.CharField(max_length=3, serialize=False, primary_key=True)),
                ('alphacode', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=100)),
                ('centerlat', models.DecimalField(max_digits=50, decimal_places=10)),
                ('centerlng', models.DecimalField(max_digits=50, decimal_places=10)),
                ('text', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'refugees_countries',
            },
        ),
        migrations.CreateModel(
            name='Refugee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('city', models.CharField(max_length=100)),
                ('num', models.IntegerField(null=True, blank=True)),
                ('year', models.CharField(max_length=4)),
                ('notes', models.TextField()),
                ('countrycode', models.ForeignKey(to='refugees.Country')),
            ],
            options={
                'db_table': 'refugees',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('stateabbr', models.CharField(max_length=2, serialize=False, primary_key=True)),
                ('statename', models.CharField(max_length=100)),
                ('statelat', models.DecimalField(max_digits=50, decimal_places=10)),
                ('statelng', models.DecimalField(max_digits=50, decimal_places=10)),
                ('stateface', models.CharField(max_length=1)),
                ('text', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'refugees_states',
            },
        ),
        migrations.AddField(
            model_name='refugee',
            name='stateabbr',
            field=models.ForeignKey(to='refugees.State'),
        ),
    ]
