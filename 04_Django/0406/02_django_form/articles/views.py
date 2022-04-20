from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

    

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        # 유효성 검사
        if form.is_valid():
            # save(): model의 save와 다른 form의 메서드이다.
            article = form.save() # return 값이 생성된 Article 객체
            return redirect('articles:detail', article.pk)

    else:
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/create.html', context)

    # title = request.POST.get('title')
    # content = request.POST.get('content')

    # article = Article(title=title, content=content)
    # article.save()

    


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article.pk)


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method =="POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            # save(): model의 save와 다른 form의 메서드이다.
            article = form.save() # return 값이 생성된 Article 객체
            return redirect('articles:detail', article.pk)
    
    else:        
        form = ArticleForm(instance=article)    
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)

    # context = {
    #     'article': article,
    # }
    
    # article.title = request.POST.get('title')
    # article.content = request.POST.get('content')
    # article.save()
    return redirect('articles:detail', article.pk)
