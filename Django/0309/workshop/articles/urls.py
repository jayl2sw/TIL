from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('<int:id>/', views.detail, name='detail'),
    path('<int:id>/edit/', views.detail_edit, name='detail_edit'),
    path('<int:id>/try_edit/', views.try_edit, name='try_edit'),
    path('<int:id>/delete/', views.delete, name='delete')
]