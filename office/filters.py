import django_filters
from .models import *
from django_filters import CharFilter
from cases.models import NeedyCase


class NeedyFilter(django_filters.FilterSet):
    name_part = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Needy
        fields = ['name', 'data_added', 'status', 'enablity', 'dependencies', 'amount']
        exclude = ['case_number', 'national_id']


class NeedyCaseFilter(django_filters.FilterSet):
    class Meta:
        model = NeedyCase
        fields = ['case_type']
