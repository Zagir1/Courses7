import django_filters as filters
from core import models


class BookFilter(filters.FilterSet):
    name = filters.CharFilter(label="Название", field_name='title', lookup_expr="icontains")
    count = filters.NumberFilter(label="Минимальное кол-во отзывов (строго больше)", field_name='num_of_reviews', lookup_expr="gt")

    class Meta:
        model = models.Book
        fields = ['title', 'num_of_reviews', ]
