import csv
from django.http import HttpResponse
from django.contrib import admin
from .models import Eleve, Livre, Emprunt

# Action personnalisée pour exporter les élèves
@admin.action(description='Exporter la sélection au format CSV')
def export_as_csv(modeladmin, request, queryset):
    meta = modeladmin.model._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename={meta}.csv'
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in queryset:
        writer.writerow([getattr(obj, field) for field in field_names])

    return response

@admin.register(Eleve)
class EleveAdmin(admin.ModelAdmin):
    list_display = ('matricule', 'nom_complet', 'classe', 'section')
    search_fields = ('nom_complet', 'matricule')
    actions = [export_as_csv] # Ajoute le bouton "Exporter"

@admin.register(Livre)
class LivreAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'titre', 'auteur', 'stock_actuel')
    search_fields = ('titre', 'isbn')
    actions = [export_as_csv] # Ajoute le bouton "Exporter"

@admin.register(Emprunt)
class EmpruntAdmin(admin.ModelAdmin):
    list_display = ('eleve', 'livre', 'date_emprunt', 'rendu')
    actions = [export_as_csv]