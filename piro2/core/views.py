from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import (Article,Comment,Tag)
# Create your views here.

#이걸 만들어야 urls.py로부터 연결이 가능해짐 이게 모델뷰의 연결
#백에서 짠 list를 보여주는 함수를 view해주는 기능.
#첫번째 게시글입니다 : 첫번째 오브젝트. 두번째 게시글입니다 : 두번째 오브젝
def article_list(request):
    article_list = Article.objects.all() #Article의 객체를 다 가져오겟다.
    ctx = {

        'article_list' : article_list,
    }
    return render(request, 'article_list.html', ctx)

#렌더링이 CRUD의 Read에 해당

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    ctx = {
        'article' : article,
    }
    return render(request,'article_detail.html', ctx)

#인자로 pk를 넘긴다는 것은, Article 객체에서 pk에 해당하는. 유니크한 값의 게시물을 보여주겠다. 는 것.
#pk는 오토 생성이니까 Article에서 보이진 않아.

def article_create(request):
    ctx = {}
    # title = request.POST.get('title')
    # content=request.POST.get('content')
    # Article.objects.create(
    #     title = title,
    #     content=content,
    #
    # )
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        if title and content:
            article = Article.objects.create(
                title=title,
                content=content,
            )
            url = reverse('core:article_detail', kwargs={
                'pk': article.pk,
            })
            return redirect(url)
        else:
            error_msg = {}
            if not title:
                error_msg.update({'title': '제목을 입력해주세요.'})
            if not content:
                error_msg.update({'content': '내용을 입력해주세요.'})
            ctx.update({'error': error_msg, })

    return render(request, 'article_create.html', ctx)