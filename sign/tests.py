from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
class LoginActionTest(TestCase):
    '''测试登录动作'''
    def setUp(self):
        User.objects.create_user('')