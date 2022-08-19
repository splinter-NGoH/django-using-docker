import django_filters as filters
from core_apps.articles.models import Article


class ArticleFilter(filter.FilterSet):
    author = filters.CharFilter(
        field_name="author__first_name", lookup_expr="icontains"
    )
    title = filters.CharFilter(field_name="title", lookup_expr="icontains")
    tags = filters.CharFilter(
        field_name="tags", method="get_article_tag", lookup_expr="iexact"
    )
    created_at = filters.IsoDateFilter(field_name="created_at")
    updated_at = filters.IsoDateFilter(field_name="updated_at")

    class Meta:
        model = Article
        fields = [
            "author",
            "title",
            "tags",
            "created_at",
            "updated_at",
        ]

    def get_article_tag(self, tags, queryset, value):
        tag_values = value.replace(" ", "").split(",")
        return queryset.filter(tags__tag__in=tag_values).distinct()
