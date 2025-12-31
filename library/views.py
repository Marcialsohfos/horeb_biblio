from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from datetime import timedelta
import json
from .models import Eleve, Livre, Emprunt

def dashboard(request):
    # Récupère les 10 derniers emprunts non rendus
    emprunts = Emprunt.objects.filter(rendu=False).order_by('-date_emprunt')[:10]
    
    # Récupère les listes pour les menus déroulants
    tous_eleves = Eleve.objects.all().order_by('nom_complet')
    tous_livres = Livre.objects.all().order_by('titre')
    
    return render(request, 'library/dashboard.html', {
        'emprunts': emprunts,
        'tous_eleves': tous_eleves,
        'tous_livres': tous_livres
    })

@csrf_exempt
def api_emprunt(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            matricule = data.get('matricule')
            isbn = data.get('isbn')

            # 1. Vérifications
            try:
                eleve = Eleve.objects.get(matricule=matricule)
            except Eleve.DoesNotExist:
                return JsonResponse({'success': False, 'message': f'Élève introuvable : {matricule}'})

            try:
                livre = Livre.objects.get(isbn=isbn)
            except Livre.DoesNotExist:
                return JsonResponse({'success': False, 'message': f'Livre introuvable : {isbn}'})

            if livre.stock_actuel <= 0:
                return JsonResponse({'success': False, 'message': 'Stock épuisé pour ce livre !'})

            # 2. Création de l'emprunt
            Emprunt.objects.create(
                eleve=eleve,
                livre=livre,
                date_retour_prevue=timezone.now() + timedelta(days=14)
            )

            # 3. Mise à jour du stock
            livre.stock_actuel -= 1
            livre.save()

            return JsonResponse({'success': True, 'message': f"Livre '{livre.titre}' prêté à {eleve.nom_complet}"})

        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Méthode non autorisée'})

@csrf_exempt
def api_retour(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            isbn = data.get('isbn')

            # Trouve le dernier emprunt non rendu pour ce livre
            # (On prend le plus ancien non rendu par logique FIFO, ou on pourrait demander le matricule)
            emprunt = Emprunt.objects.filter(livre__isbn=isbn, rendu=False).first()

            if not emprunt:
                return JsonResponse({'success': False, 'message': "Ce livre n'est pas marqué comme sorti !"})

            # Valider le retour
            emprunt.rendu = True
            emprunt.date_retour_reelle = timezone.now()
            emprunt.save()

            # Remettre en stock
            livre = emprunt.livre
            livre.stock_actuel += 1
            livre.save()

            return JsonResponse({'success': True, 'message': f"RETOUR OK : {livre.titre} (Élève: {emprunt.eleve.nom_complet})"})

        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Méthode non autorisée'})