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
    article = Article.objects.get(pk=id)
    article.delete()
    
    return redirect('articles:index')
