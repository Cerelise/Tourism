from django_filters import rest_framework as filters

from .models import AttractionsArticle


class ArticleFilter(filters.FilterSet):

    scentic = filters.CharFilter(field_name='scentic',lookup_expr='exact')

    class Meta:
        model = AttractionsArticle
        fields = ['scentic']