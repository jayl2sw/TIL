# Workshop
### Article CR (CREATE & READ) 

CR을 갖춘 장고 프로젝트를 제작하고, 결과 사진과 핵심 코드(url, view, template, model)를 별도의 마크다운 파일에 작성하여 제출하시오. 



* urls.py

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
      path('new', views.new, name='new'),
      path('create', views.create, name='create'),
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
      return redirect('../articles/', DEBUG=False)
  ```

  

* templates >base.html

  ```django
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Workshop</title>
  </head>
  <body>
    <div class="container">
      {% block content %}
      {% endblock content %}
    </div>
  </body>
  </html>
  ```

  

* templates > articles > index.html

  ```django
  {% extends 'base.html' %}
  
  {% block content %}
  <h1>INDEX</h1>
  
  <a href="{% url 'articles:new' %}">NEW</a>
  <br>
  {% for article in articles %}
    <h2>제목 :{{ article.title }}</h2>
    <p>내용 :{{ article.content }}</p>
  {% endfor %}
  
  <a href="">Detail</a>
  {% endblock content %}
  ```

  

* templates > articles > new.html

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

  

  