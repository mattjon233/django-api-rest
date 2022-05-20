from rest_framework import serializers
from .models import Asset, VulnerabilityInAsset
from vulnerabilities.serializers import VulnerabilitySerializer


class AssetSerializer(serializers.ModelSerializer):
    '''
    Serializer contendo a função get_vulnerabilities_count para fins de visualização
    '''
    vulnerabilities_count = serializers.SerializerMethodField()

    class Meta:
        model = Asset
        fields = ('hostname', 'ip', 'vulnerabilities_count', 'risk_factor')
    
    def get_vulnerabilities_count(self, obj):
        return obj.vulnerabilities.count()


class VulnerabilityInAssetSerializer(serializers.ModelSerializer):
    '''
    Serializer contendo apenas o campo solved (aparecerá apenas o campo solved)
    '''
    class Meta:
        model = VulnerabilityInAsset
        fields = ('solved', )


class VulnerabilityInAssetDetailSerializer(serializers.ModelSerializer):
    '''
    Serializer auxiliar para VulnerabilityInAsset, ele serve para listar todos os campos
    quando se está decidindo se quer marcar ou não como resolvida
    '''
    asset = AssetSerializer(read_only=True)
    vulnerability = VulnerabilitySerializer(read_only=True)
    
    class Meta:
        model = VulnerabilityInAsset
        fields = '__all__'
