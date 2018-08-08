from django.contrib.auth.models import User
from django.db import models

# Create your models here.
#models 모듈안의 Model클래 상속

class Tag(models.Model):
    name = models.CharField(max_length=10, verbose_name='태그')
    def __str__(self):
        return self.name
#태그로 아티클을 찾는 경우가 많다.(반대경우보다) 그래서 태그를 위에두고,
#아티클 안에 태그를 매니투매니로 적어둔다. 그러면 쿼리셋을 쏠때가 다른데,
#쿼리셋을 Article.get.object() 이런식으로 태그를 쏘게 된다.
#Tag.get.object 이런식으로 하는게 아니라. ->여기 질문.
#manytomany는 내용물이 많은 클래스에 넣어주면 편하다 그냥.


class Article(models.Model):
    title = models.CharField(max_length=20, verbose_name= '제목')
    content = models.TextField(verbose_name='내용')
    # author = models.OneToOneField(User)
    author= models.CharField(max_length=10, verbose_name='저자')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    tag = models.ManyToManyField(Tag)
    #온딜리트는 필요없다. 아티클이 지워져도, 다른 태그가 지워지는 관계가 아니니까.

    def __str__(self):
        return self.title


class Comment(models.Model):
    content = models.TextField(verbose_name = '댓글')
    author = models.CharField(max_length=10, verbose_name='글쓴이')
    article = models.ForeignKey(Article, on_delete= models.CASCADE)

