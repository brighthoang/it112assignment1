from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
from django.contrib.auth.models import User
import datetime
# from .forms import ProductForm
# from django.urls import reverse_lazy, reverse

class MeetingTest(TestCase):
    def setUp(self):
        self.all = Meeting(meetingtitle = 'DEA Meeting', meetingdate = datetime.date(2022, 5, 13), meetingtime = datetime.time(12, 30),
        location = 'Los Angeles', agenda = "Eating tofu soup and enjoying RUN BTS!")

    def test_typestring(self):
        self.assertEqual(str(self.all), "DEA Meeting")

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table), 'meeting')


class MeetingMinutesTest(TestCase):
    def setUp(self):
        self.min = MeetingMinutes(minutestext = '')

    def test_typestring(self):
        self.assertEqual(str(self.min), '')

    def test_tablename(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table), 'meetingminutes')


class ResourceTest(TestCase):
    def setUp(self):
        self.type = Resource(resourcename = 'Boxes', resourcetype = "Objects", url = "https://www.amazon.com/uBoxes-Moving-Boxes-Bundle-Medium/dp/B08ZFZ8TPR/ref=sr_1_omk_6?crid=24WUIL7IBSJ4H&keywords=boxes&qid=1652501559&sprefix=%2Caps%2C153&sr=8-6",
        dateentered = datetime.date(2022, 4, 20), description = "Brown cardboard boxes that can hold up to 200 pounds.")

    def test_typestring(self):
        self.assertEqual(str(self.type), 'Boxes')

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table), 'resource')

class EventTest(TestCase):
    def setUp(self):
        self.events = Event(eventtitle = "Moon Festival 2022", location = "Portland, WA", date = datetime.date(2022, 8, 22), time = datetime.time(8, 00),
        description = "Fun event for families to enjoy.")

    def test_typestring(self):
        self.assertEqual(str(self.events), 'Moon Festival 2022')

    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table), 'event')
