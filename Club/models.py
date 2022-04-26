from django.db import models
from django.forms import CharField, DateField
from django.contrib.auth.models import User

class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField(max_length=255)
    meetingtime=models.TimeField(max_length=255)
    location=models.CharField(max_length=255)
    agenda=models.CharField(max_length=255)

    def __str__(self):
        return self.meetingtitle

    class Meta:
        db_table='meeting'


class MeetingMinutes(models.Model):
    meetingid=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    attendance=models.ManyToManyField(User)
    minutestext=models.TextField(null=True, blank=True)

    def __str__(self):
        return self.minutestext

    class Meta:
        db_table='meetingminutes'

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255)
    url=models.URLField(null=True, blank=True)
    dateentered=models.DateField()
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description=models.TextField()

    def __str__(self):
        return self.resourcename

    class Meta:
        db_table='resource'


class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    location=models.CharField(max_length=255)
    date=models.DateField()
    time=models.TimeField()
    description=models.TextField()
    userid=models.CharField(max_length=255) # i really dont know how to do that part.

    def __str__(self):
        return self.eventtitle

    class Meta:
        db_table='event'

