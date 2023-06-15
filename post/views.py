from rest_framework import generics
from rest_framework.exceptions import PermissionDenied
from .models import Article
from .permissions import IsAuthorOrReadOnly, IsPublicReadOnly, IsSubscriberOrReadOnly
from .serializers import ArticleSerializer


class ArticleList(generics.ListCreateAPIView):
    """
    View to list all articles or create a new article.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update or delete an article.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def update(self, request, *args, **kwargs):
        article = self.get_object()
        if article.author != request.user:
            raise PermissionDenied("You don't have permission to edit this article")
        return super().update(request, *args, **kwargs)


class PublicArticleList(generics.ListAPIView):
    """
    View to list all public articles.
    """
    queryset = Article.objects.filter(access='public')
    serializer_class = ArticleSerializer
    permission_classes = [IsPublicReadOnly]


class SubscriberArticleList(generics.ListAPIView):
    """
    View to list all articles for subscribers.
    """
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsSubscriberOrReadOnly]