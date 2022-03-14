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
      path('create/', views.create, name='create'),
      path('<int:article_pk>/', views.detail, name='detail'),
      path('<int:article_pk>/detail_edit/', views.detail_edit, name='detail_edit'),
      path('<int:article_pk>/delete/', views.delete, name='delete'),
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
  
  def create(request):
      if request.method == "POST":
          title = request.POST.get('title')
          content = request.POST.get('content')
  
          article = Article(title=title, content=content)
          article.save()
          return redirect('articles:index')
      
      return render(request,'articles/form.html')
      
  def detail(request, article_pk=None):
      article = Article.objects.get(pk=article_pk)
      context = {
          'article':article,
      }
      return render(request, 'articles/detail.html', context)
  
  def detail_edit(request, article_pk=None):
      article = Article.objects.get(pk=article_pk)
      
      if request.method == 'POST':
          title = request.POST.get('title')
          content = request.POST.get('content')
          
          article.title = title
          article.content = content
          article.save()
          
          return redirect('articles:detail', article.pk)
      
      else:
          context = {
              'article':article,
          }   
  
      return render(request, 'articles/form.html', context)
  
  def delete(request, article_pk):
      if request.method == "POST":
          article = Article.objects.get(pk=article_pk)
          article.delete()
          return redirect('articles:index')
  
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
  <hr>
  <a href="{% url 'articles:create' %}">NEW</a>
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

  

* articles > form.html

  ```django
  {% extends 'base.html' %}
  
  {% block content %}
    {% if request.resolver_match.url_name == 'create' %}
      <h1>NEW</h1>
    {% else %}
      <h1>EDIT</h1>
    {% endif %}  
    <hr>
  
    <form action="" method="POST">
      {% csrf_token %}
      <label for="title" >TITLE:</label>
      <input type="text" id='title' name='title' value={{ article.title }}>
      <br>
      <div class="d-flex align-items-start">
        <label for="content">CONTENT: </label>
        <textarea name="content" id="content" cols="30" rows="10">{{ article.content }}</textarea>
      </div>
      <br>
      <div class="grid">
        {% if request.resolver_match.url_name == 'create' %}
          <input type="submit" value='작성'>
          <a href="{% url 'articles:index' %}">BACK</a>
        {% else %}
          <input type="submit" value='수정'>
          <a href="{% url 'articles:detail' article.pk %}">BACK</a>
        {% endif %}
      </div>
    </form>
    
  {% endblock content %}
  ```

  

* articles > detail.html

  ```django
  {% extends 'base.html' %}
  
  {% block content %}
    <h1>DETAIL</h1>
    <hr>
    <div class="d-flex align-items-baseline">
      <h2>{{ article.title }}</h2>
      {% if article.created_at != article.updated_at %}<span class="fs-6 mx-1">[수정됨]</span>{% endif %}
    </div>
    
    <p>{{ article.content }}</p>
    <p>작성일: {{ article.created_at }}</p>
    <p>수정일: {{ article.updated_at }}</p>
  
    <div class="d-flex">
      <form action="{% url 'articles:detail_edit' article.pk %}">
        <input type="submit" value="EDIT">
      </form>
      <form action="{% url 'articles:delete' article.pk %}" method="POST" class="mx-1">
        {% csrf_token %}
        <input type="submit" value="DELETE">
      <a href="{% url 'articles:index' %}">BACK</a>   
    </div>
    </form>
    
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

  