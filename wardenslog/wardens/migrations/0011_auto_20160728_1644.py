# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wardens', '0010_auto_20160728_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='warning_issued',
            field=models.CharField(max_length=50, null=True, choices=[('YES', 'Yes'), ('No', 'No')]),
        ),
    ]
