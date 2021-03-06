from django.urls import path
# 단, 장고에서는 명시적 경로를 작성해주어야 한다.
from . import views

app_name = 'articles'

urlpatterns = [
    path('index/', views.index, name="index"),
    path('throw/', views.throw, name="throw"),
    path('catch/', views.catch, name="catch"),
    path('random-user/', views.randomuser, name="randomuser"),
    # <datatype: variable_name> 
    # variable_name과 view의 keyword argument이름이 같아야 한다.
    path('hello/<str:name>/', views.hello, name="hello"),
]