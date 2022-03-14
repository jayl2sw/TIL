from django.shortcuts import render
from .models import Article
# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)


def new(request):
    return render(request, 'articles/new.html')


def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    
    # 첫 번째 방법
    
    article = Article()
    article.title=title 
    article.content=content

    articles = Article.objects.all()
    context = {
        'articles':articles,
    }

    if len(title) <= 10:
        article.save()
        return index(request)
    else:
        return render(request, 'articles/new.html')


    # 두 번째 방법
    '''
    article = Article(title=title, content=content)
    article.save()

    return render(request, 'articles/create.html')
    '''
    
    # 세 번째 방법
    '''
    Article.objects.create(title=title, content=content)
    return render(request, 'article/create.html')
    '''
