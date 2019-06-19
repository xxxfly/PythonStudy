from django.shortcuts import render
from django.http import HttpResponse
from  datetime import  datetime

# Create your views here.


def home(request):
    param={
        'title': "主页",
        'year': datetime.now().year
    }
    return render(request, 'user/index.html', param)


def about(request):
    param = {
        'title': "about",
        'year': datetime.now().year
    }
    return render(request, 'user/about.html', param)


def contact(request):
    param = {
        'title': "contact",
        'year': datetime.now().year
    }
    return render(request, 'user/contact.html', param)


def loginpartial(request):
    return render(request, 'user/loginpartial.html')


def add(request, id):
    param = {
        'uid': id
    }
    return render(request, 'user/useradd.html', param)
