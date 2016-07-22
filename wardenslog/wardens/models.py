from __future__ import unicode_literals

from django.db import models


class Site(models.Model):   #site model containing all relevant information regarding site
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Hall(models.Model):   #Hall model containing all relevant information regarding student
    name = models.CharField(max_length=40)
    site = models.ForeignKey(Site, related_name='halls')

    def __str__(self):
        return self.name


class Student(models.Model):                        #student model. containing all relevant information regarding student
    banner_id = models.CharField(max_length=12)
    surname = models.CharField(max_length=60)
    forename = models.CharField(max_length=60)
    site = models.CharField(max_length=30)
    hall = models.CharField(max_length=30)
    room_number = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s' % (self.surname, self.forename)


class IncidentType(models.Model):   #Model for the type of incident at hand
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type


class Incident(models.Model):       # all fields related to creating an incident report and/or viewing cases i.e closed
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    warden_name = models.CharField(max_length=150)
    senior_warden = models.CharField(max_length=150)
    site = models.ForeignKey(Site, related_name='incidents')
    incident_type = models.ForeignKey(IncidentType, related_name='incidents')
    halls = models.ForeignKey(Hall, related_name='incidents')
    status = models.CharField(max_length=250)
    description = models.TextField()

    notes_to = models.TextField(null=True, blank=True)
    notes_by = models.TextField(null=True, blank=True)
    warning_issued = models.CharField(max_length=250, null=True, blank=True)
    disciplinary_required = models.NullBooleanField(null=True, blank=True)
    disciplinary_called_by = models.CharField(max_length=150, null=True, blank=True)
    disciplinary_date = models.DateTimeField(null=True, blank=True)
    student = models.ForeignKey(Student, related_name='incidents')
    complainant = models.CharField(max_length=500, null=True, blank=True)
    accomplices = models.CharField(max_length=500, null=True, blank=True)
    witnesses = models.CharField(max_length=500, null=True, blank=True)



