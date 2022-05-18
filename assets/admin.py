from django.contrib import admin
from .models import Asset, VulnerabilityInAsset


# visualização dos dados no painel de administração
class AssetAdmin(admin.ModelAdmin):
    list_display = ('hostname', 'ip', 'risk_factor')
    list_filter = ('risk_factor', )
    search_fields = ('hostname', 'ip')


class VulnerabilityInAssetAdmin(admin.ModelAdmin):
    list_display = ('asset', 'vulnerability', 'solved')
    list_filter = ('asset', 'vulnerability', 'solved')


admin.site.register(Asset, AssetAdmin)
admin.site.register(VulnerabilityInAsset, VulnerabilityInAssetAdmin)
