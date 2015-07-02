# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_userlike'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlike',
            name='uname',
            field=models.CharField(max_length=128),
        ),
    ]
