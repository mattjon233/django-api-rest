from django.db import models
from vulnerabilities.models import Vulnerability


class Asset(models.Model):
    '''
    Modelagem dos assets, contendo os fields necessários para a API
    '''
    hostname = models.CharField(max_length=60)
    ip = models.CharField(max_length=15)
    vulnerabilities = models.ManyToManyField(Vulnerability, through='VulnerabilityInAsset')
    risk_factor = models.FloatField(default=0)


class VulnerabilityInAsset(models.Model):
    '''
    Modelagem das vulnerabilidades resolvidas, contendo os fields necessários para a API
    '''
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    vulnerability = models.ForeignKey(Vulnerability, on_delete=models.CASCADE)
    solved = models.BooleanField(default=False)
