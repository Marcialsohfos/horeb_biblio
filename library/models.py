from django.db import models
from django.utils import timezone

class Eleve(models.Model):
    # Gestion du bilinguisme
    SECTION_CHOICES = [('FR', 'Francophone'), ('EN', 'Anglophone')]
    
    matricule = models.CharField(max_length=20, unique=True, help_text="Scanner ou entrer manuellement")
    nom_complet = models.CharField(max_length=200)
    classe = models.CharField(max_length=50, help_text="Ex: 6ème, Form 1, Tle D")
    section = models.CharField(max_length=2, choices=SECTION_CHOICES, default='FR')
    photo = models.ImageField(upload_to='photos_eleves/', blank=True, null=True) # Optionnel
    
    def __str__(self):
        return f"{self.nom_complet} ({self.classe})"

class Livre(models.Model):
    CATEGORIES = [
        ('MANUEL', 'Manuel Scolaire'),
        ('ROMAN', 'Roman / Fiction'),
        ('REVUE', 'Revue / Magazine'),
        ('DICO', 'Dictionnaire'),
    ]
    
    isbn = models.CharField(max_length=20, unique=True, help_text="Code barre du livre")
    titre = models.CharField(max_length=200)
    auteur = models.CharField(max_length=100)
    categorie = models.CharField(max_length=10, choices=CATEGORIES, default='MANUEL')
    stock_total = models.PositiveIntegerField(default=1)
    stock_actuel = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return f"{self.titre} (Dispo: {self.stock_actuel})"

class Emprunt(models.Model):
    eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE)
    date_emprunt = models.DateTimeField(default=timezone.now)
    date_retour_prevue = models.DateField()
    rendu = models.BooleanField(default=False)
    date_retour_reelle = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.eleve.nom_complet} -> {self.livre.titre}"