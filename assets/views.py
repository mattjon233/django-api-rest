from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from .filters import AssetFilterSet, VulnerabilityInAssetFilterSet
from .models import Asset, VulnerabilityInAsset
from .serializers import AssetSerializer, VulnerabilityInAssetSerializer, VulnerabilityInAssetDetailSerializer


class AssetViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
    # ordenando por maiores risk_factors primeiro
    ordering = ['-risk_factor']
    search_fields = ['hostname', 'ip']
    ordering_fields = ['risk_factor']
    filter_class = AssetFilterSet


class VulnerabilityInAssetViewSet(mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = VulnerabilityInAsset.objects.all()
    serializer_class = VulnerabilityInAssetSerializer
    filter_class = VulnerabilityInAssetFilterSet

    def get_serializer_class(self):
        if self.action in ['retrieve', 'list']:
            return VulnerabilityInAssetDetailSerializer
        return super().get_serializer_class()
