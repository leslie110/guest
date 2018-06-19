from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from sign.models import Event

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

@login_required()
def search_name(requeest):
    username = requeest.session.get('user','')
    search_name = requeest.GET.get('name','')
    event_list = Event.objects.filter(name__contains=search_name)
    return render(requeest,"event_manage.html",{"user":username,
                                                "events":event_list})
