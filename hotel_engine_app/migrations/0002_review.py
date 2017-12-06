# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 18:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel_engine_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=1000, verbose_name='Şərh')),
                ('rate', models.IntegerField(verbose_name='Qiymət')),
                ('by_whom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel_engine_app.Customer', verbose_name='Fikir bildirən')),
                ('to_hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel_engine_app.Hotel', verbose_name='Otel')),
            ],
            options={
                'verbose_name': 'Fikir',
                'verbose_name_plural': 'Fikirlər',
            },
        ),
    ]
