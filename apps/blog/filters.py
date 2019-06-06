

import django_filters
from django.db.models import Q

from .models import Article


class ArticleFilter(django_filters.rest_framework.FilterSet):

    search_category = django_filters.CharFilter(method='category_filter')
    search_tag = django_filters.CharFilter(method='tag_filter')


    def category_filter(self, queryset, name, value):
        return queryset.filter(Q(category__name=value))

    def tag_filter(self, queryset, name, value):
        return queryset.filter(Q(tag__name=value))





