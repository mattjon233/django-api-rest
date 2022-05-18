from .models import Vulnerability
from django_filters import FilterSet


class VulnerabiltyFilterSet(FilterSet):
    class Meta:
        model = Vulnerability
        fields = ('cvss', 'severity')
