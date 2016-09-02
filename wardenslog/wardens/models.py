from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from django.db import models


class Site(models.Model):   #site model containing all relevant information regarding site
    name = models.CharField(_('Name'), max_length=100)

    def __str__(self):
        return self.name


class Hall(models.Model):   #Hall model containing all relevant information regarding student
    name = models.CharField(_('Name'), max_length=40)
    site = models.ForeignKey(Site, related_name='halls')

    def __str__(self):
        return self.name


class Student(models.Model):                        #student model. containing all relevant information regarding student
    banner_id = models.CharField(_('banner id'), max_length=12)
    surname = models.CharField(_('surname'), max_length=60)
    forename = models.CharField(_('forename'), max_length=60)
    site = models.CharField(_('Site'), max_length=30)
    hall = models.CharField(_('Hall'), max_length=30)
    room_number = models.CharField(_('Room Number'), max_length=50)

    def __str__(self):
        return '%s %s' % (self.surname, self.forename)


class IncidentType(models.Model):   #Model for the type of incident at hand
    type = models.CharField(_('Type'), max_length=50)

    def __str__(self):
        return self.type


class Incident(models.Model):       # all fields related to creating an incident report and/or viewing cases i.e closed
    title = models.CharField(_('title'), max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    warden_name = models.CharField(_('warden name'), max_length=150)
    senior_warden = models.CharField(_('senior warden'), max_length=150)
    site = models.ForeignKey(Site, related_name='incidents')
    halls = models.ForeignKey(Hall, related_name='incidents')
    incident_type = models.ForeignKey(IncidentType, related_name='incidents')
    ACTIVE = 'Active'
    CLOSED = 'Closed'
    CASE_STATUS = (
        (ACTIVE, 'Active'),
        (CLOSED, 'Closed'),
    )
    case_status = models.CharField(
        max_length=50,
        choices=CASE_STATUS,
        default=ACTIVE
    )
    description = models.TextField()
    notes_to = models.TextField(null=True, blank=True)
    notes_by = models.TextField(null=True, blank=True)
    YES = 'YES'
    NO = 'No'
    WARNING_ISSUED = (
        (YES, 'Yes'),
        (NO, 'No'),
    )
    warning_issued = models.CharField(
        null=True,
        max_length=50,
        choices=WARNING_ISSUED,
        default=YES
    )
    YES = 'Yes'
    NO = 'No'
    DISCIPLINARY_REQUIRED = (
        (YES, _('Yes')),
        (NO, _('No')),
    )
    disciplinary_required = models.CharField(
        null=True,
        max_length=50,
        choices=DISCIPLINARY_REQUIRED,
        default=YES
    )
    disciplinary_called_by = models.CharField(_('disciplinary called by'), max_length=150, null=True, blank=True)
    disciplinary_date = models.DateTimeField(_('disciplinary date'), null=True, blank=True)
    student = models.ForeignKey(Student, related_name='incidents')
    complainant = models.CharField(_('complainant'), max_length=500, null=True, blank=True)
    accomplices = models.CharField(_('accomplices'), max_length=500, null=True, blank=True)
    witnesses = models.CharField(_('witnesses'), max_length=500, null=True, blank=True)



