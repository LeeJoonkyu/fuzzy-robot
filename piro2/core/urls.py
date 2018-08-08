from django.urls import path

from . import views

app_name='core'

urlpatterns=[
    path('article_list',views.article_list,name='article_list'),
    path('article/<int:pk>', views.article_detail, name='article_detail'),
    path('article/create/', views.article_create, name='article_create'),
]

#<int로 받은 값을 : pk에 넣겠다>
#<str : title>
#해줄수도있다.