# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 11:51
from __future__ import unicode_literals

from django.db import migrations, models
import simplemde.fields


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0010_auto_20170225_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=simplemde.fields.SimpleMDEField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='project',
            name='body',
            field=simplemde.fields.SimpleMDEField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='summary',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
