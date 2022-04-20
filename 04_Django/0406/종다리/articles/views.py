from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()

    context ={
        'articles': articles
    }
    return render(request, 'articles/index.html', context)


def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, '게시글이 생성되었습니다.')
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form': form 
    }
    return render(request, 'articles/create.html', context)


def update(request, id):
    article = Article.objects.get(id = id)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance = article)
        if form.is_valid():
            form.save()
            messages.info(request, '게시글이 업데이트 되었습니다.')
            return redirect('articles:index')
    else:
        form = ArticleForm(instance = article)
    context = {
        'form': form
    }
    return render(request, 'articles/update.html', context)


def delete(request, id):
    article = Article.objects.get(id=id)
    article.delete()
    messages.info(request, '게시글이 삭제 되었습니다.')
    return redirect('articles:index')
    