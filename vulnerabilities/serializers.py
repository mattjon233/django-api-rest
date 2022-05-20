from rest_framework import serializers
from .models import Vulnerability


class VulnerabilitySerializer(serializers.ModelSerializer):
    '''
    O serializer das vulnerabilidades contendo a função que retorna o número de assets daquela vulnerabilidade
    com os campos totais (além do assets_count)
    '''
    assets_count = serializers.SerializerMethodField()

    class Meta:
        model = Vulnerability
        fields = ('title', 'severity', 'cvss', 'publication_date', 'assets_count')
    
    def get_assets_count(self, obj):
        return obj.asset_set.count()
