from django.shortcuts import render

# Create your views here.
def index(request): # 필수 인자 http request 객체
    return render(request, 'index.html') # request, template,