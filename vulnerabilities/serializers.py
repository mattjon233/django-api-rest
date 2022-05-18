from rest_framework import serializers
from .models import Vulnerability


class VulnerabilitySerializer(serializers.ModelSerializer):
    assets_count = serializers.SerializerMethodField()

    class Meta:
        model = Vulnerability
        fields = ('title', 'severity', 'cvss', 'publication_date', 'assets_count')
    
    def get_assets_count(self, obj):
        return obj.asset_set.count()
