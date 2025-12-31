from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from datetime import timedelta
from .models import Eleve, Livre, Emprunt
import json

def dashboard(request):
    emprunts = Emprunt.objects.filter(rendu=False).order_by('-date_emprunt')[:10]
    # On envoie tous les élèves et livres pour les listes déroulantes
    tous_eleves = Eleve.objects.all().order_by('nom_complet')
    tous_livres = Livre.objects.all().order_by('titre')
    
    return render(request, 'library/dashboard.html', {
        'emprunts': emprunts,
        'tous_eleves': tous_eleves,
        'tous_livres': tous_livres
    })

# ... (Gardez les fonctions api_emprunt et api_retour telles quelles) ...
# ... Copiez le code api_emprunt et api_retour de votre ancien fichier views.py ...