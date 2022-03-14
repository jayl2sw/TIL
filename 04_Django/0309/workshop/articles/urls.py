from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/', views.detail, name='detail'),
    path('<int:article_pk>/detail_edit/', views.detail_edit, name='detail_edit'),
    path('<int:article_pk>/delete/', views.delete, name='delete'),
]