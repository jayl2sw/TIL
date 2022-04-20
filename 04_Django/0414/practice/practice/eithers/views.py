from django.views.decorators.http import require_http_methods,require_POST, require_safe
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from random import choice
from django.db.models import Q, Count

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.order_by('-created_at')[:20]
    context = {
        'articles': articles,
    }    
    return render(request, 'eithers/index.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('eithers:detail', article.pk)

    else:
        form = ArticleForm()

    context = {
        'form': form,
    }
    return render(request, 'eithers/create.html', context)


# @require_safe
# def detail(request, pk):
#     comment_form = CommentForm()
#     articles = Article.objects.order_by('-created_at')[:10]
#     total_count = Count('comment')
#     count_b = Count('comment', filter=Q(comment__color=0))
#     count_r = Count('comment', filter=Q(comment__color=1))
#     result = Article.objects.annotate(
#                             total_count=total_count,
#                             count_a=count_b,
#                             count_b=count_r
#                         )
#     # annotate에 작성된 칼럼을 만들어줌
#     article = get_object_or_404(result, pk=pk)
#     comments = article.comment_set.order_by('-pk')

#     blue_p = round(article.count_b / article.total_count * 100, 2) if article.total_count else 0
#     red_p = round(article.count_r / article.total_count * 100, 2) if article.total_count else 0
#     context = {
#         'articles' : articles,
#         'article': article,
#         'comment_form': comment_form,
#         'comments': comments,
#         'blue_p':blue_p,
#         'red_p':red_p,
#     }
#     return render(request, 'eithers/detail.html', context)

@require_safe
def detail(request, pk):
    articles = Article.objects.order_by('-created_at')[:10]
    article = get_object_or_404(Article, pk=pk)
    comments = article.comment_set.all()
    article.vws += 1
    article.save()
    comment_form = CommentForm
    _blue = article.blue_score
    _red = article.red_score
    blue_p = round(_blue / (_blue + _red) * 100, 1) if _blue + _red != 0 else 0
    red_p = round(_red / (_blue + _red) * 100, 1) if _blue + _red != 0 else 0
    

    context = {
        'articles' : articles,
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
        'blue_p':blue_p,
        'red_p':red_p,
    }
    return render(request, 'eithers/detail.html', context)

@require_POST
def delete(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        if request.user == article.user:
            article.delete()
    return redirect('eithers:index')

@require_POST
def create_comment(request, pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article
            comment.user = request.user
            comment.save()
            if comment.color == False:
                article.red_score += 1    
            else:
                article.blue_score += 1
            article.save()
        print(comment_form.errors)
        return redirect('eithers:detail', article.pk)
        
    return redirect('accounts:login')

@require_POST
def delete_comment(request, pk, comment_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=pk)
        comment = get_object_or_404(Comment, pk=comment_pk)
        if request.user == comment.user:
            print(comment.color)
            if comment.color == False:
                article.red_score -= 1    
            else:   
                article.blue_score -= 1
            article.save()
            comment.delete()
    return redirect('eithers:detail', article.pk)
    
@require_safe
def random(request):
    articles = Article.objects.all().values('pk')
    print(articles)
    return redirect('eithers:detail', choice(articles)['pk'])
    