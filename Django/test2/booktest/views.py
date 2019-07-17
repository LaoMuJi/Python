from django.shortcuts import render
from .models import BookInfo
# Create your views here.

def index(request):

    # 查询图书的信息
    books = BookInfo.objects.all()

    return render(request, 'booktest/index.html', {'books':books})

