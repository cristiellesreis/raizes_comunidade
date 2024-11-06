from django.contrib import admin
from .models import Horta, Cultura, SolicitacaoAcesso, Plantio

class ParticipanteInline(admin.TabularInline):
    model = Horta.participantes.through 
    extra = 1  

@admin.register(Horta)
class HortaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'usuario', 'descricao', 'comunitaria')
    search_fields = ('nome', 'usuario__username')
    list_filter = ('comunitaria',)
    inlines = [ParticipanteInline]

    fieldsets = (
        (None, {
            'fields': ('nome', 'descricao', 'usuario', 'comunitaria')
        }),
    )
    exclude = ('participantes',)



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

@admin.register(SolicitacaoAcesso)
class SolicitacaoAcessoAdmin(admin.ModelAdmin):
    list_display = ('horta', 'usuario_solicitante', 'data_solicitacao', 'aprovado')
    search_fields = ('horta', 'usuario_solicitante')
    list_filter = ('horta',)
    
    fieldsets = (
        (None, {
            'fields': ('horta', 'usuario_solicitante', 'aprovado')
        }),
    )
    
@admin.register(Plantio)
class PlantioAdmin(admin.ModelAdmin):
    list_display = ('cultura', 'usuario', 'descricao', 'horta')
    search_fields = ('cultura__name', 'horta__nome')
    list_filter = ('horta',)

    fieldsets = (
        (None, {
            'fields': ('cultura__name', 'descricao', 'horta')
        }),
    )
