# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-04 03:36
from __future__ import unicode_literals

import django.contrib.auth.validators
from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20170929_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to='avatars', verbose_name='Avatar'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]