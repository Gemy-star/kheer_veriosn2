import django_filters
from .models import *
from django_filters import CharFilter


class NeedyFilter(django_filters.FilterSet):
    name_part = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Needy
        fields = ['name',  'data_added', 'status', 'enablity', 'dependencies', 'amount']
        exclude = ['case_number', 'national_id']
