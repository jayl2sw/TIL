from django.shortcuts import render, redirect, get_object_or_404
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html', context)

def create(request):
    # 사용자가 POST 요청을 보냈다면...
    if request.method == 'POST':
        # GET 요청으로 보내진 데이터는
        # title = request.GET.get('title') # QueryDict
        # content = request.GET.get('content') # QueryDict
        # print(dir(request))
        title = request.POST.get('title') # QueryDict
        content = request.POST.get('content') # QueryDict

        '''
        Article.objects.create(title=title, content=content)
        '''
        article = Article()
        article.title = title
        article.content = content
        # db에 반영
        article.save()
        
        # POST 요청에 맞게 게시글을 생성하고 난 후,
        # return render(request, 'articles/index.html')
        # redirect(path)
        # 경로가 수정 될 경우, redirect에 작성한 경로도 수정해야한다.
        # detail 페이지는 article_pk를 필요로 한다.
        return redirect('articles:detail', article.pk)
    # 아니면?
    # else:
        # GET 요청이 왔으니 html 문서를 보여주자...
        # 뭘 보여줄까?
    return render(request, 'articles/form.html')

def detail(request, article_pk):
    # article_pk 번째 게시글의 정보를 조회, 반영
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)

def delete(request, article_pk):
    # 특정 게시글 조회
    # article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        article = get_object_or_404(Article, pk=article_pk)
        article.delete()
    return redirect('articles:index')

def update(request, article_pk):
    # article = Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('articles:detail', article.pk)
    else:
        context = {
            'article': article
        }
    return render(request, 'articles/form.html', context)
