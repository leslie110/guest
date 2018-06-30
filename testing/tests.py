# -*- coding:utf-8 -*-
from django.test import TestCase
from sign.models import Event,Guest
# create your tests here
class ModelTest(TestCase):

    def setUp(self):
        Event.objects.create(id=1,name="oneplus 3 event",status=True,limit=2000,address='sz',start_time='2018-05-09 09:57:11')
        Guest.objects.create(id=1,event_id=1,realname='alen',phone='13700000000',email="alen@mail.com",sign=False)
    # def test_event_modles(self):
    #     result = Event.objects.get(name='oneplus 3 event')
    #     self.assertEqual(result.address,'sz')
    #     self.assertTrue(result.status)

    def test_guest_modles(self):
        result = Guest.objects.get(phone='13700000000')
        self.assertEqual(result.realname,'alen')
        self.assertFalse(result.sign)

    def tearDown(self):
        pass