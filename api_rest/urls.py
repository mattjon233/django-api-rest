from django.contrib import admin
from django.urls import path, include

api_urls = [
    path('', include('assets.urls'), name='assets'),
    path('', include('vulnerabilities.urls'), name='vulnerabilities'),
    path('', include('core.urls'), name='core')
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urls), name='api')
]
