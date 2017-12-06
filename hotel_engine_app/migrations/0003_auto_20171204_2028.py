# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 20:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_engine_app', '0002_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='manager',
            name='birth_date',
        ),
        migrations.RemoveField(
            model_name='receptionist',
            name='birth_date',
        ),
        migrations.AlterField(
            model_name='hotel',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel_engine_app.Manager', verbose_name='Otelin meneceri'),
        ),
    ]
