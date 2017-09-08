# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-08 03:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0015_auto_20170908_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='about',
            name='published_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
