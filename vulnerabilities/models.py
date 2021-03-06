from django.db import models


class Vulnerability(models.Model):
    '''
    Modelagem das vulnerabilidaes, especificando título, severity, cvss e data de publicação
    '''
    title = models.TextField()
    severity = models.CharField(max_length=10)
    cvss = models.FloatField(default=None, blank=True, null=True)
    publication_date = models.DateField(default=None, blank=True, null=True)

    def __str__(self):
        return self.title
