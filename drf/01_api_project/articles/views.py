from django.shortcuts import get_object_or_404, render

from .models import Article
from .serializers import ArticleListSerializer,ArticleSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def article_list(request):
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def article_detail(request,article_pk):
    article = get_object_or_404(Article,pk=article_pk)
    serializer = ArticleSerializer(article)
    return Response(serializer.data)