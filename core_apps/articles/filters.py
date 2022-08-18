import django_filters as filters
from core_apps.articles.models import Article


class ArticleFilter(filter.FilterSet):
    author = filters.CharFilter(field_name="author__first_name", lookup_expr="icontains")
    title = filters.CharFilter