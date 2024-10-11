from django.contrib import admin
from django.contrib.auth.models import Group
from django.apps import apps

def criar_grupo():
    Group.objects.get_or_create('Comum')
    
    Group.objects.get_or_create("Líder Comunitário")
    
    
if apps.ready:
    criar_grupo()