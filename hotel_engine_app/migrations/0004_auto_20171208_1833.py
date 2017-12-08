# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-08 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_engine_app', '0003_auto_20171204_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='contact_info',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='hotel',
            name='guest_capacity',
            field=models.IntegerField(default=80, verbose_name='Nömrələrin sayı'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='room_capacity',
            field=models.IntegerField(default=50, verbose_name='Nömrələrin sayı'),
        ),
    ]
