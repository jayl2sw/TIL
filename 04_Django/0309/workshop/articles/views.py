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
