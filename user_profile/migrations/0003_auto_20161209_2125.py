# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-09 21:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20161201_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='activation_key',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='profile',
            name='key_expires',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
