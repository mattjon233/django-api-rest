from .models import Asset, VulnerabilityInAsset
from django_filters import FilterSet


class AssetFilterSet(FilterSet):
    '''
    Filtrando por risk_factor, parâmetro necessário na API
    '''
    class Meta:
        model = Asset
        fields = ('risk_factor', )

 
class VulnerabilityInAssetFilterSet(FilterSet):
    '''
    Filtrando vulnerabilidadeinasset em vulnerability, asset e solved (se a vulnerabilidade foi resolvida)
    '''
    class Meta:
        model = VulnerabilityInAsset
        fields = ('vulnerability', 'asset', 'solved')