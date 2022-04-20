from django.urls import path
from . import views
app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:articleId>/', views.detail, name='detail'),
    path('<int:articleId>/update', views.update, name='update'),
    path('<int:articleId>/delete', views.delete, name='delete'),
]