from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class LivreForm(ModelForm):
    class Meta:
        model = models.Livre
        fields = ('titre', 'auteur', 'date_parution', 'nombres_pages','resume')
        labels = {
            'titre' : _('Titre'),
            'auteur' : _('Auteur') ,
            'date_parution' : _('date␣de␣parution'),
            'nombres_pages' : _('nombres␣de␣pages'),
            'resume' : _('Résumé')
        }

class BibliothequeForm(ModelForm):
    class Meta:
        model = models.Bibliotheque
        fields = ('Universite', 'Region', 'Departement', 'nombres_de_livres')
        labels = {
            'Universite': _('Universite'),
            'Region': _('Region'),
            'Departement': _('Departement'),
            'nombres_de_livres': _('nombres_de_livres'),
        }


