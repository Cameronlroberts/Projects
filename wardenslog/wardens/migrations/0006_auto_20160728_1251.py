# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wardens', '0005_auto_20160728_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='Case_Status',
            field=models.CharField(max_length=500, choices=[('Active', 'Active'), ('Active', 'Closed')]),
        ),
    ]
