from email import message
from django.shortcuts import render
import random

# Create your views here.
def throw(request):
    return render(request, 'articles/throw.html')


def catch(request):
    message = request.GET.get('message')
    context = {
        'message': message,
    }
    return render(request,'articles/catch.html', context)

def hello(request, name):
    context = {
        'name': name
    }
    return render(request, 'articles/hello.html', context)

def index(request):
    return render(request, 'articles/index.html')


def randomuser(request):
    userlist = ['김구현', '김지현', '서상균', '홍성목']
    user = random.choice(userlist)
    context = {
        'user': user
    }
    return render(request, 'articles/randomuser.html', context)