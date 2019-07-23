from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'booktest/index.html')


def show_arg(request,num):
    return HttpResponse(num)


def login(request):
    return render(request, 'booktest/login.html')


def login_check(request):
    '''
    request.POST    request.GET
    传过来的类似字典，允许一个名字对应多个值
    '''
    username = request.POST.get('username')
    password = request.POST.get('password')


    # print(request.path) # 显示请求的完整路径，不包含域名
    # print(request.method) # 显示HTTP请求方法，get，post


    if username == '0' and password == '0':
        return redirect('/index')
    else:
        return redirect('/login')