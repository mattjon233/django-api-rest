from typing import Type
import pandas as pd
from datetime import datetime
from vulnerabilities.models import Vulnerability
from assets.models import Asset
from rest_framework.response import Response
from django.http import JsonResponse

def csv_create(request):
    # import ipdb; ipdb.set_trace()
    data = pd.read_csv('asset_vulnerability.csv').to_dict('records')
    
    # linha a linha
    for i in data:
        # vulnerabilities
        title_vul = i['VULNERABILITY - TITLE']
        severity_vul = i['VULNERABILITY - SEVERITY']
        cvss_vul = i['VULNERABILITY - CVSS']
        date_vul = i['VULNERABILITY - PUBLICATION_DATE']
        # assets
        hostname_ast = i['ASSET - HOSTNAME']
        ip_ast = i['ASSET - IP_ADDRESS']

        # checando se a coluna data tem nome
        date_vul_aux = datetime.strptime(date_vul, '%Y-%m-%d') if isinstance(date_vul, str) else None
        
        # a vulnerabilidade já existe?
        # se sim, usar no asset
        # se não, criar e usar no asset
        new_vulnerability = None

        try:
            new_vulnerability = Vulnerability.objects.get(title=title_vul)
        # caso de não existir
        except Vulnerability.DoesNotExist:
            new_vulnerability = Vulnerability.objects.create(
                title=title_vul,
                severity=severity_vul,
                cvss=cvss_vul,
                publication_date=date_vul_aux
            )
        # caso haja mais de uma vulnerabilidade com o mesmo nome, retorna o primeiro (casos excepcionais)
        except Vulnerability.MultipleObjectsReturned:
            new_vulnerability = Vulnerability.objects.filter(title=title_vul).first()

        # busca o asset com o hostname e ip dado, e cria caso não haja
        new_asset = Asset.objects.get_or_create(
            hostname=hostname_ast,
            ip=ip_ast
        )[0]

        # checando se o cvss da vulnerabilidade é maior que o risk factor
        # se sim, alterá-lo
        try:
            if new_asset.risk_factor < new_vulnerability.cvss:
                new_asset.risk_factor = new_vulnerability.cvss
                new_asset.save()
        except TypeError:
            new_asset.risk_factor = 0
            new_asset.save()

        # adicionando na lista de vulnerabilidades a nova vulnerabilidade
        new_asset.vulnerabilities.add(new_vulnerability)

    return JsonResponse({'msg':'Importado com sucesso!'})
