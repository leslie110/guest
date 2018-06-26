from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from sign.models import Event,Guest
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
#登录首页
def login(request):
    #return HttpResponse("Heloo Django")
    return render(request,"login.html")

def indexs(requset):
    return render(requset,"indexs.html")
#登录动作
'''
def login_action(request):
    if request.method == "POST":
        username = request.POST.get("username",'')
        password = request.POST.get("password",'')
        if username == 'admin' and password == "admin123":
            response =  HttpResponseRedirect(r'event_manage/')
            # response.set_cookie('user',username,3600)#添加浏览器cookie
            request.session['user'] = username #将session信息记录到浏览器
            return response
        else:
            return render(request,"login.html",{'error':"用户名或者密码不正确！！"})
            '''
def login_action(request):
    if request.method == "POST":
        username = request.POST.get("username",'')
        password = request.POST.get("password",'')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            request.session['user'] = username #将session信息记录到浏览器

            response =  HttpResponseRedirect(r'/event_manage/')
            return response
        else:
            return render(request,"login.html",{'error':"用户名或者密码不正确！！"})

#发布会管理
@login_required
def event_manage(request):
    #username = request.COOKIES.get('user','')#读取浏览器cookie
    event_list = Event.objects.all()
    username = request.session.get('user','')
    return render(request,'event_manage.html',{'user':username,
                                               "events":event_list})
# 发布会名称搜索
@login_required()
def search_name(request):
    username = request.session.get('user','')
    search_name = request.GET.get('name','')
    event_list = Event.objects.filter(name__contains=search_name)
    return render(request,"event_manage.html",{"user":username,
                                                "events":event_list})

# 嘉宾管理
@login_required()
def guest_manage(request):
    username = request.session.get('user','')
    guest_list = Guest.objects.all()
    paginator = Paginator(guest_list,2)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        #如果page不是整数，取第一页面数据
        contacts = paginator.page(1)
    except EmptyPage:
        #如果page不在范围，取最后一页面
        contacts = paginator.page(paginator.num_pages)
    return render(request,"guest_manage.html",{"user":username,
                                               "guests":contacts
    })