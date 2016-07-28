# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wardens', '0008_auto_20160728_1255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='incident',
            name='disciplinary_required',
        ),
        migrations.AddField(
            model_name='incident',
            name='Disciplinary_required',
            field=models.CharField(max_length=50, null=True, choices=[('YES', 'Yes'), ('No', 'No')]),
        ),
    ]
