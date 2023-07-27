import django_filters
from .models import Car


class CarFilter(django_filters.FilterSet):
    model = django_filters.CharFilter(field_name='model', lookup_expr='icontains', label='Модель')

    class Meta:
        model = Car
        fields = ['brand', 'model', 'year']
