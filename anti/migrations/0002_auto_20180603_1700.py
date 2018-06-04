# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-03 14:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anti', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='description',
            new_name='report_incident',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='editor',
            new_name='reporter',
        ),
        migrations.RemoveField(
            model_name='report',
            name='report',
        ),
        migrations.AddField(
            model_name='report',
            name='position_of_offender',
            field=models.CharField(max_length=60, null=True),
        ),
    ]