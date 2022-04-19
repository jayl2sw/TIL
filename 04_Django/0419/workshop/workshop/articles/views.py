from django.shortcuts import render,redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
# Create your views here.
def index(request):
    articles = Article.objects.all()
    context ={
        'articles':articles
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method=="POST":
        form  = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            
        return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/create.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk = article_pk)
    context ={
        'article':article
    }
    return render(request, 'articles/detail.html', context)

def like(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk = article_pk)
        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
        return redirect('articles:detail', article.pk)
    return redirect('accounts:login')