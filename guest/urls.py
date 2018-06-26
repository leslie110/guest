"""guest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from sign import views#导入应用模块

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r"^login/$",views.login),#添加index/路径配置
    url(r"indexs/",views.indexs),
    url(r"login_action",views.login_action),
    url(r"event_manage/",views.event_manage),
    url(r"^$",views.login),
    url(r'accounts/login/$',views.login),
    url(r"^search_name/$",views.search_name),
    url(r"^guest_manage/",views.guest_manage),
]
