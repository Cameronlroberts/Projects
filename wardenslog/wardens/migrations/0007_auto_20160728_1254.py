# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wardens', '0006_auto_20160728_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='Case_Status',
            field=models.CharField(max_length=50, choices=[('Active', 'Active'), ('Active', 'Closed')]),
        ),
    ]
