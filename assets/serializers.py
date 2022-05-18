from rest_framework import serializers
from .models import Asset, VulnerabilityInAsset
from vulnerabilities.serializers import VulnerabilitySerializer


class AssetSerializer(serializers.ModelSerializer):
    vulnerabilities_count = serializers.SerializerMethodField()

    class Meta:
        model = Asset
        fields = ('hostname', 'ip', 'vulnerabilities_count', 'risk_factor')
    
    def get_vulnerabilities_count(self, obj):
        return obj.vulnerabilities.count()


class VulnerabilityInAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = VulnerabilityInAsset
        fields = ('solved', )


class VulnerabilityInAssetDetailSerializer(serializers.ModelSerializer):
    # exibir essas tabelas no response
    asset = AssetSerializer(read_only=True)
    vulnerability = VulnerabilitySerializer(read_only=True)
    
    class Meta:
        model = VulnerabilityInAsset
        fields = '__all__'
