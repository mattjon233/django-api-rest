from django.db import models
from vulnerabilities.models import Vulnerability


class Asset(models.Model):
    hostname = models.CharField(max_length=60)
    ip = models.CharField(max_length=15)
    vulnerabilities = models.ManyToManyField(Vulnerability, through='VulnerabilityInAsset')
    risk_factor = models.FloatField(default=0)


class VulnerabilityInAsset(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    vulnerability = models.ForeignKey(Vulnerability, on_delete=models.CASCADE)
    solved = models.BooleanField(default=False)
