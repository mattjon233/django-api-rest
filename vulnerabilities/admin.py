from django.contrib import admin
from .models import Vulnerability


# visualização dos dados no painel de administração
class VulnerabilityAdmin(admin.ModelAdmin):
    list_display = ('title', 'severity', 'cvss', 'publication_date')
    list_filter = ('severity', 'cvss')
    search_fields = ('title', )


admin.site.register(Vulnerability, VulnerabilityAdmin)
