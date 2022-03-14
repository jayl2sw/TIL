from re import A
from django.urls import path
from . import views

app_name = 'lotto'

urlpatterns = [
    path('lotto/', views.lotto, name="lotto"),
    path('lottop/', views.lotto_p, name="lottop"),
]

