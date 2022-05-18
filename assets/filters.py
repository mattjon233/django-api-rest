from .models import Asset, VulnerabilityInAsset
from django_filters import FilterSet


class AssetFilterSet(FilterSet):
    class Meta:
        model = Asset
        fields = ('risk_factor', )


class VulnerabilityInAssetFilterSet(FilterSet):
    class Meta:
        model = VulnerabilityInAsset
        fields = ('vulnerability', 'asset', 'solved')