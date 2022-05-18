from .views import csv_create
from django.urls import path

urlpatterns = [
    path('upload_csv', csv_create, name='upload_csv')
]