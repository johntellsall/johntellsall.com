from django.contrib.auth.models import User
from django.db import models


class MeetupUser(User):
    pass


class Meeting(models.Model):
    name = models.CharField(max_length=100)
    meet_date = models.DateTimeField()
    attendee = models.ManyToManyField(MeetupUser)

