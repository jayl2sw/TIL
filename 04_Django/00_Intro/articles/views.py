from django.shortcuts import render
import random

# Create your views here.
def index(request): # 필수 인자 http request 객체
    return render(request, 'index.html') # request, template,

def greeting(request):
    foods = ['apple', 'banana', 'coconut']
    info = {
        'name': 'Alice',
    }
    context = {
        'foods' : foods,
        'info' : info
    }
    return render(request, 'greeting.html', context)

def dinner(request):
    foods =['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(foods)
    context = {
        'pick' : pick,
        'foods' : foods,
    }
    return render(request, 'dinner.html', context)

def dtl_practice(request):
    foods =['족발', '햄버거', '치킨', '초밥']
    fruits = ['apple', 'banana', 'cucumber', 'mango']
    user_list = []
    context = {
        'foods' : foods,
        'fruits' : fruits,
        'user_list' : user_list,
    }
    return render(request, 'dtl_practice.html', context)
