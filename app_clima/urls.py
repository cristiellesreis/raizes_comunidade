from django.urls import path
from app_clima.views import  clima
urlpatterns = [
    path('clima', clima, name='clima'),
]