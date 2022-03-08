# Workshop

* crud > urls.py

  ```python
  """crud URL Configuration
  
  The `urlpatterns` list routes URLs to views. For more information please see:
      https://docs.djangoproject.com/en/3.2/topics/http/urls/
  Examples:
  Function views
      1. Add an import:  from my_app import views
      2. Add a URL to urlpatterns:  path('', views.home, name='home')
  Class-based views
      1. Add an import:  from other_app.views import Home
      2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
  Including another URLconf
      1. Import the include() function: from django.urls import include, path
      2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
  """
  from django.contrib import admin
  from django.urls import path, include
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('articles/', include('articles.urls'))
  ]
  ```

  

* articles > urls.py

  ```python
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
  ```

  

* views.py

  ```python
  from django.shortcuts import render, redirect
  from crud.settings import DEBUG
  from .models import Article
  
  # Create your views here.
  def index(request):
      articles = Article.objects.all()
      
      context = {
          'articles': articles,
      }
      return render(request, 'articles/index.html', context)
  
  
  def new(request):
      return render(request, 'articles/new.html')
  
  def create(request):
      title = request.GET.get('title')
      content = request.GET.get('content')
  
      article = Article(title=title, content=content)
      article.save()
      return redirect('articles:index')
  
  def detail(request, id=None):
      article = Article.objects.get(pk=id)
      context = {
          'article':article,
      }
      return render(request, 'articles/detail/detail.html', context)
  
  def detail_edit(request, id=None):
      article = Article.objects.get(pk=id)
      context = {
          'article':article,
      }
      return render(request, 'articles/detail/detail_edit.html', context)
  
  def try_edit(request, id=None):
      article = Article.objects.get(pk=id)
  
      title = request.GET.get('title')
      content = request.GET.get('content')
      
      article.title = title
      article.content = content
      article.save()
      return redirect('articles:index')
  
  def delete(request, id=None):
      print(id)
      article = Article.objects.get(pk=id)
      article.delete()
      
      return redirect('articles:index')
  ```

  

* base.html

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <title>Workshop</title>
  </head>
  <body>
    <div class="container">
      {% block content %}
      {% endblock content %}
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
  </body>
  </html>
  ```

  

* articles > index.html

  ```django
  {% extends 'base.html' %}
  
  {% block content %}
  <h1>INDEX</h1>
  <br>
  <a href="{% url 'articles:new' %}">NEW</a>
  <br>
  <br>
  {% for article in articles %}
    <h2>제목 :{{ article.title }}</h2>
    <p>내용 :{{ article.content }}</p>
    <a href="{% url 'articles:detail' article.pk%}">Detail</a>
    <hr>
    <br>
  {% endfor %}
  
  {% endblock content %}
  ```

  

* articles > new.html

  ```django
  {% extends 'base.html' %}
  
  {% block content %}
    <h1>NEW</h1>
    <form action="{% url 'articles:create' %}">
      <label for="title">TITLE: </label>
      <input type="text" id='title' name='title'>
      <br>
      <label for="content">CONTENT: </label>
      <textarea name="content" id="content" cols="30" rows="30"></textarea>
      <br>
      <input type="submit" value='작성'>
    </form>
    <a href="{% url 'articles:index' %}">BACK</a>
  {% endblock content %}
  ```

  

* articles > detail > detail.html

  ```django
  {% extends 'base.html' %}
  
  {% block content %}
    <h1>DETAIL</h1>
    <hr>
    <h2>{{ article.title }}</h2>
    <p>{{ article.content }}</p>
    <p>작성일: {{ article.created_at }}</p>
    <p>수정일: {{ article.updated_at }}</p>
  
    <a href="{% url 'articles:detail_edit' article.pk %}">EDIT</a> <a href="{% url 'articles:delete' article.pk %}">DELETE</a>
    <a href="{% url 'articles:index' %}">BACK</a>
    
  {% endblock content %}
  ```

  

* articles > detail > detail_edit.html

  ```django
  {% extends 'base.html' %}
  
  {% block content %}
    <h1>EDIT</h1>
    <form action="{% url 'articles:try_edit' article.pk %} ">
      <label for="title">TITLE:</label>
      <input type="text" id='title' name='title' value={{ article.title }}>
      <br>
      <label for="content">CONTENT: </label>
      <textarea name="content" id="content" cols="30" rows="30">{{ article.content }}</textarea>
      <br>
      <input type="submit" value='수정'>
    </form>
    <a href="{% url 'articles:detail' article.pk %}">BACK</a>
  {% endblock content %}
  ```

  

* models.py

  ```python
  from django.db import models
  
  # Create your models here.
  class Article(models.Model):
      title = models.CharField(max_length=10)
      content = models.TextField()
      created_at = models.DateTimeField(auto_now_add=True)
      updated_at = models.DateTimeField(auto_now=True)
  
      def __str__(self):
          return self.title
  ```

  