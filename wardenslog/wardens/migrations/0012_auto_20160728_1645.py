# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wardens', '0011_auto_20160728_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='Disciplinary_required',
            field=models.CharField(default='YES', max_length=50, null=True, choices=[('YES', 'Yes'), ('No', 'No')]),
        ),
        migrations.AlterField(
            model_name='incident',
            name='warning_issued',
            field=models.CharField(default='YES', max_length=50, null=True, choices=[('YES', 'Yes'), ('No', 'No')]),
        ),
    ]
