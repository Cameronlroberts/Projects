# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wardens', '0002_auto_20160721_1647'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incident',
            name='status',
        ),
        migrations.AddField(
            model_name='incident',
            name='Case_Status',
            field=models.CharField(default='ACT', max_length=2, choices=[('ACT', 'Active'), ('CLO', 'Closed')]),
        ),
        migrations.AlterField(
            model_name='incident',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
