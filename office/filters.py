import django_filters
from .models import *
from django_filters import CharFilter


class CourseFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='iexact')

    class Meta:
        model = Courses
        fields = ['start_date', 'end_date', 'name']


class NeedyFilter(django_filters.FilterSet):
    name_part = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Needy
        fields = ['source_income','home','health_status']
        exclude = ['case_number', 'national_id']
