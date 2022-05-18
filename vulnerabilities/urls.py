from .views import VulnerabilityViewSet
from django.urls import path
from rest_framework.routers import DefaultRouter

# se no final da url haverá uma barra ou não
router = DefaultRouter(trailing_slash=False)
# primeiro parametro: nome que aparecerá na url
router.register('vulnerabilities', VulnerabilityViewSet, 'vulnerabilities')
urlpatterns = router.urls
