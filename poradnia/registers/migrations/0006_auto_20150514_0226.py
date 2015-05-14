# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0005_advice_case'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advice',
            name='case',
            field=models.OneToOneField(null=True, blank=True, to='cases.Case'),
            preserve_default=True,
        ),
    ]
