# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-10-23 13:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20191023_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authordetail',
            name='phone',
            field=models.CharField(max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='publish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Publish', unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='publish',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
