# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2019-10-23 13:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20191023_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Publish'),
        ),
    ]
