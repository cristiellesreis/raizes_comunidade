from django.contrib import admin
from .models import Horta, Cultura

@admin.register(Horta)
class HortaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'usuario', 'descricao', 'comunitaria')
    search_fields = ('nome', 'usuario__username')
    list_filter = ('comunitaria',)
    
    fieldsets = (
        (None, {
            'fields': ('nome', 'descricao', 'usuario', 'comunitaria')
        }),
    )

@admin.register(Cultura)
class CulturaAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'desc', 'horta')
    search_fields = ('name', 'horta__nome')
    list_filter = ('horta',)

    fieldsets = (
        (None, {
            'fields': ('name', 'type', 'desc', 'horta')
        }),
    )
