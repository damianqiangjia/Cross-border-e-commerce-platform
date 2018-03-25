# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-07 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20171128_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dsahboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(max_length=64)),
                ('order_number', models.CharField(max_length=64)),
                ('order_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='OrderCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=64)),
                ('order_count', models.IntegerField()),
                ('product_count', models.IntegerField()),
                ('allprice', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Predict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=64)),
                ('order_count', models.IntegerField()),
                ('naifen_Aptamil', models.IntegerField()),
                ('naifen_Gallia', models.IntegerField()),
                ('naifen_Babybio', models.IntegerField()),
                ('muying_Hipp', models.IntegerField()),
                ('hufu_Herbacin', models.IntegerField()),
                ('hufu_Balea', models.IntegerField()),
                ('hufu_Schaebens', models.IntegerField()),
                ('shipin_Hipp', models.IntegerField()),
                ('richang_Brita', models.IntegerField()),
                ('richang_Facelle', models.IntegerField()),
                ('baojian_Salus', models.IntegerField()),
                ('baojian_Doppelherz', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=64)),
                ('naifen_Aptamil', models.IntegerField()),
                ('naifen_Gallia', models.IntegerField()),
                ('naifen_Babybio', models.IntegerField()),
                ('muying_Hipp', models.IntegerField()),
                ('hufu_Herbacin', models.IntegerField()),
                ('hufu_Balea', models.IntegerField()),
                ('hufu_Schaebens', models.IntegerField()),
                ('shipin_Hipp', models.IntegerField()),
                ('richang_Brita', models.IntegerField()),
                ('richang_Facelle', models.IntegerField()),
                ('baojian_Salus', models.IntegerField()),
                ('baojian_Doppelherz', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TypeCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=64)),
                ('naifen_count', models.IntegerField()),
                ('muying_count', models.IntegerField()),
                ('hufu_count', models.IntegerField()),
                ('shipin_count', models.IntegerField()),
                ('richang_count', models.IntegerField()),
                ('baojian_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WorldAreaData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('value', models.IntegerField()),
            ],
        ),
    ]