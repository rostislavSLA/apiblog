from django.urls import path
from .views import ArticleList, ArticleDetail, PublicArticleList, SubscriberArticleList

urlpatterns = [
    path('articles/', ArticleList.as_view(), name='article-list'),
    path('articles/<int:pk>/', ArticleDetail.as_view(), name='article-detail'),
    path('articles/public/', PublicArticleList.as_view(), name='public-article-list'),
    path('articles/subscriber/', SubscriberArticleList.as_view(), name='subscriber-article-list'),
]