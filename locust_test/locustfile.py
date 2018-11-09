# coding=utf-8
from locust import HttpLocust,TaskSet,task

# web性能测试
class UserBehavior(TaskSet):

    def on_start(self):
        '''
        每次登录操作
        :return:
        '''
        self.login()


    def login(self):
        self.client.post("/login_action",{"username":"admin",
                                          "password":"admin"})

    @task(2)
    # @task()装饰的方法为一个事物，数字越大每次被虚拟用户执行的概率越高，不设置默认为1
    def event_manage(self):
        self.client.get("/event_manage")

    @task(2)
    def guest_manage(self):
        self.client.get("/guest_manage")


class WebsitueUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 0
    max_wait = 0