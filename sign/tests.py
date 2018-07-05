# -*- coding:utf-8 -*-
from django.test import TestCase
from sign.models import Event,Guest
from django.contrib.auth.models import User
# create your tests here
class ModelTest(TestCase):

    def setUp(self):
        Event.objects.create(id=1,name="oneplus 3 event",status=True,limit=2000,address='sz',start_time='2018-05-09 09:57:11')
        Guest.objects.create(id=1,event_id=1,realname='alen',phone='13700000000',email="alen@mail.com",sign=False)

    def test_event_modles(self):
        result = Event.objects.get(name='oneplus 3 event')
        self.assertEqual(result.address,'sz1')
        self.assertTrue(result.status)

    def test_guest_modles(self):
        result = Guest.objects.get(phone='13700000000')
        self.assertEqual(result.realname,'alen1')
        self.assertFalse(result.sign)

    def tearDown(self):
        pass

class IndexPageTest(TestCase):
    '''测试index登录首页'''
    def test_index_page_renders_index_template(self):
        '''测试index试图'''
        response = self.client.get('/login/')
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'login.html')


class LonginActionnTest(TestCase):
    '''测试登录动作'''
    def setUp(self):
        User.objects.create_user('root','root@qq.com','root123')

    def test_add_admin(self):
        '''测试添加用户'''
        user = User.objects.get(username='root')
        self.assertEqual(user.username,'root')
        self.assertEqual(user.email,'root@qq.com')
    def test_login_action_uesrname_password_null(self):
        '''测试登录密码为空'''
        test_data = {'username':'','password':''}
        response = self.client.post('/login_action/',data=test_data)
        self.assertEqual(response.status_code,200)
        self.assertIn(b"username or password error",response.content)

    def test_login_action_username_password_error(self):
        '''测试登录密码错误'''
        test_data = {'username':'root','password':'rootttt'}
        response = self.client.post('/login_action/',data=test_data)
        self.assertEqual(response.status_code,200)
        print (response.content)
        self.assertIn(b'username or password error',response.content)
    def test_action_username_password(self):
        '''登录成功'''
        test_data = {'username':"root",'password':"root123"}
        response = self.client.post('/login_action',data=test_data)
        self.assertEqual(response.status_code,302)

class EventManageTest(TestCase):
    '''发布会管理'''
    def setUp(self):
        User.objects.create_user('root', 'root@qq.com', 'root123')
        Event.objects.create(id=1, name="xiaomi5", status=True, limit=2000, address='beijing',
                             start_time='2018-05-09 09:57:11')
        self.login_user = {'username':'root','password':'root123'}

    def test_event_manage_success(self):
        '''测试发布会：xiaomi5'''
        respons = self.client.post('/login_action/',data=self.login_user)
        response = self.client.post('/event_manage/')
        self.assertEqual(response.status_code,200)
        self.assertIn(b'xiaomi5',response.content)
        self.assertIn(b'beijing',response.content)

    def test_event_manage_serach_success(self):
        '''测试发布会搜索'''
        respons = self.client.post('/login_action',data=self.login_user)
        response = self.client.post('/search_name/',{"name":'xiaomi5'})
        self.assertEqual(response.status_code,200)
        self.assertIn(b"xiaomi5",response.content)
        self.assertIn(b"beijing",response.content)




