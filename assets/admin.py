from django.contrib import admin
from .models import Asset, VulnerabilityInAsset


class AssetAdmin(admin.ModelAdmin):
    '''
    Responsável pela visualização dos dados de assets no painel de administração
    '''
    list_display = ('hostname', 'ip', 'risk_factor')
    list_filter = ('risk_factor', )
    search_fields = ('hostname', 'ip')


class VulnerabilityInAssetAdmin(admin.ModelAdmin):
    '''
    Responsável pela visualização dos dados de vulnerabilidde no painel de administração
    '''
    list_display = ('asset', 'vulnerability', 'solved')
    list_filter = ('asset', 'vulnerability', 'solved')


# registrando no painel
admin.site.register(Asset, AssetAdmin)
admin.site.register(VulnerabilityInAsset, VulnerabilityInAssetAdmin)
