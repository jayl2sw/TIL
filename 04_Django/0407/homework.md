# Homework

### 아래 작성된 views.py의 코드 일부를 보고 문제에 알맞은 답을 서술하시오.

```python
from django.shortcuts import render, redirect
from .forms import ArticleForm

def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid:
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form  = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/create.html', context)
```



1. 왜 변수 context는 if else 구문과 동일한 레벨에 작성 되어있는가? 

   ```python
   request.method가 POST인 경우 
   만약, form 내의 데이터가 유효성 검사를 통과하지 못했을 때, 해당 form의 정보와 에러를 포함하여 다시 articles/create.html로 렌더링 해주기 위함이다.
   ```

   

2. 왜 request의 http method는 POST 먼저 확인하도록 작성하는가

   ```python
   reqeust의 http method에는 POST, PUT, PATCH, DELETE 등 다양한 방법이 있다.
   POST는 데이터베이스에 접근하는 method인데 GET을 먼저 확인하고 else를 하게 되면 POST가 아닌 다른 method가 왔을때에도 데이터베이스에 접근될 수 있기 때문에 POST먼저 확인하게 된다.
   * 더 예민한 처리이기 때문에 확실하게 조건분기 해주기 위함
   ```

   