# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wardens', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incident',
            old_name='IncidentType',
            new_name='incident_type',
        ),
        migrations.RemoveField(
            model_name='incident',
            name='disciplinary_called',
        ),
        migrations.AddField(
            model_name='incident',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 21, 11, 26, 28, 961981, tzinfo=utc), auto_created=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='incident',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 21, 11, 26, 45, 141765, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='incident',
            name='description',
            field=models.TextField(default='x'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='incident',
            name='disciplinary_called_by',
            field=models.CharField(max_length=150, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='incident',
            name='disciplinary_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='incident',
            name='disciplinary_required',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='incident',
            name='notes_by',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='incident',
            name='notes_to',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='incident',
            name='status',
            field=models.CharField(default='x', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='incident',
            name='warning_issued',
            field=models.CharField(max_length=250, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='accomplices',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='complainant',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='incident',
            name='witnesses',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='room_number',
            field=models.CharField(max_length=50),
        ),
    ]
