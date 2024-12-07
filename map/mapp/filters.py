import django_filters as df
from .models import *

# class ProductFilter(django_filters.FilterSet):
#     name = django_filters.CharFilter(lookup_expr='icontains', label='Название')
#     category = django_filters.ChoiceFilter(choices=[
#         ('electronics', 'Электроника'),
#         ('books', 'Книги'),
#         ('clothing', 'Одежда'),
#         # Добавьте другие категории по необходимости
#     ], label='Категория')
#     price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gte', label='Цена от')
#     price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label='Цена до')
#
#     class Meta:
#         model = Product
#         fields = ['name', 'category', 'price__gt', 'price__lt']


class LogFilter(df.FilteSet):
    actor = df.CharFilter(lookup_expr='icontains', label='Действователь')

    class Meta:
        model = Log
        fields = ['actor']