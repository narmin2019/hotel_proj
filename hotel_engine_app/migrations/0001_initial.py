# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 17:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Doğum tarixi')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Sistem istifadəçisi')),
            ],
            options={
                'verbose_name': 'Müştəri',
                'verbose_name_plural': 'Müştərilər',
            },
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Adı')),
                ('region', models.CharField(blank=True, max_length=30)),
                ('price', models.IntegerField(verbose_name='Qiymət')),
                ('photo', models.ImageField(upload_to='', verbose_name='Şəkil')),
            ],
            options={
                'verbose_name': 'Otel',
                'verbose_name_plural': 'Otellər',
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Doğum tarixi')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Sistem istifadəçisi')),
            ],
            options={
                'verbose_name': 'Otel meneceri',
                'verbose_name_plural': 'Otel menecerləri',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField(blank=True, null=True, verbose_name='Giriş vaxtı')),
                ('to_date', models.DateField(blank=True, null=True, verbose_name='Çıxış vaxtı')),
                ('number_of_rooms', models.IntegerField(default=1, verbose_name='Nömrələrin sayı')),
                ('number_of_guest', models.IntegerField(default=1, verbose_name='Qonaqların sayı')),
                ('is_approved', models.BooleanField(default=False, verbose_name='Təstiq statusu')),
                ('by_whom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Sifarişçi')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel_engine_app.Hotel', verbose_name='Otel')),
            ],
            options={
                'verbose_name': 'Sifariş',
                'verbose_name_plural': 'Sifarişlər',
            },
        ),
        migrations.CreateModel(
            name='Receptionist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Doğum tarixi')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel_engine_app.Hotel', verbose_name='İşlədiyi otel')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Sistem istifadəçisi')),
            ],
            options={
                'verbose_name': 'Resepşn',
                'verbose_name_plural': 'Resepşnlar',
            },
        ),
        migrations.AddField(
            model_name='hotel',
            name='manager',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='hotel_engine_app.Manager', verbose_name='Otelin meneceri'),
        ),
    ]
