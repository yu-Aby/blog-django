from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action, detail_route

from blog.filters import ArticleFilter
from .serializers import ArticleSerializers,TagSerializers,CategorySerializers

from rest_framework import mixins, filters
from rest_framework import generics
from .models import Article,Tag,Category
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination



class AllPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class ArticleListViewSet(viewsets.ModelViewSet):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializers
    pagination_class = AllPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = ArticleFilter
    search_fields = ('title','content')

class TagListViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers


class CategoryListViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers










