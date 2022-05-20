from .models import Vulnerability
from django_filters import FilterSet


class VulnerabiltyFilterSet(FilterSet):
    '''
    Filtrando pelos valores de severity e cvss
    '''
    class Meta:
        model = Vulnerability
        fields = ('cvss', 'severity')
