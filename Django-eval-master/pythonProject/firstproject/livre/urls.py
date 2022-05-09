from django.urls import path
from . import views
urlpatterns = [
    path('formulaire', views.formulaire, name='formulaire'),
    path('traitement/', views.traitement),
    path("",views.index),
    path("affiche/<int:id>/",views.affiche),
    path("update/<int:id>/",views.update),
    path("updatetraitement/<int:id>/",views.updatetraitement),
    path("delete/<int:id>/",  views.delete),
    path("accueil/", views.accueil),
    path("formulairebibliotheque/", views.formulairebibliotheque),
    path("affichebibliotheque/<int:id>/", views.affichebibliotheque),
    path ("traitementbibliotheque/", views.traitementbibliotheque),
    path("updatebibliotheque/<int:id>/", views.updatebibliotheque),
    path("updatetraitementbibliotheque/<int:id>/", views.updatetraitementbibliotheque),
    path ("deletebibliotheque/<int:id>/", views.deletebibliotheque)

]

