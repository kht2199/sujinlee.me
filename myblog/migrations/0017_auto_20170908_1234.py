# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-08 03:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myblog', '0016_auto_20170908_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='body',
        ),
        migrations.AddField(
            model_name='about',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='about',
            name='text',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='about',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
