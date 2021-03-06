import django_filters
from django.db.models import Q
from .models import Goods


class GoodsFillter(django_filters.rest_framework.FilterSet):
    pricemin = django_filters.NumberFilter(field_name='shop_price', help_text="min price", lookup_expr='gte')
    pricemax = django_filters.NumberFilter(field_name='shop_price', help_text="max price", lookup_expr='lte')
    top_category = django_filters.NumberFilter(method='top_category_filter')

    def top_category_filter(self, queryset, name, value):
        return queryset.filter(Q(category_id=value) | Q(category__parent_category_id=value) | Q(
            category_parent_category_parent_category_id=value))

    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax', 'is_hot', 'is_new']
