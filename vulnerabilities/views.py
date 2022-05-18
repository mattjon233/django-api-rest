from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .filters import VulnerabiltyFilterSet
from .models import Vulnerability
from .serializers import VulnerabilitySerializer


class VulnerabilityViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Vulnerability.objects.all()
    serializer_class = VulnerabilitySerializer
    # ordenando por maiores cvss primeiro
    ordering = ['-cvss']
    search_fields = ['title']
    ordering_fields = ['cvss', 'severity']
    filter_class = VulnerabiltyFilterSet
