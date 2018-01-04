# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-04 03:36
from __future__ import unicode_literals

from django.db import migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tasty_feedback', '0002_auto_20150802_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='status_changed',
            field=model_utils.fields.MonitorField(default=django.utils.timezone.now, monitor='status', verbose_name='Status change date'),
        ),
    ]
