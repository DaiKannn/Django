from django.urls import path
from . import views
urlpatterns = [
    path('accueilcsgo/', views.accueilcsgo),
    path('formulairecsgo/', views.formulairecsgo, name='formulaire'),
    path('traitementcsgo/', views.traitementcsgo),
    path("affichecsgo/<int:id>/",views.affichecsgo),
    path("updatecsgo/<int:id>/",views.updatecsgo),
    path("updatetraitementcsgo/<int:id>/",views.updatetraitementcsgo),
    path("deletecsgo/<int:id>/",  views.deletecsgo),
    #path("accueil/", views.accueil),
    #path("formulairebibliotheque/", views.formulairebibliotheque),
    #path("affichebibliotheque/<int:id>/", views.affichebibliotheque),
    #path ("traitementbibliotheque/", views.traitementbibliotheque),
    #path("updatebibliotheque/<int:id>/", views.updatebibliotheque),
    #path("updatetraitementbibliotheque/<int:id>/", views.updatetraitementbibliotheque),
    #path ("deletebibliotheque/<int:id>/", views.deletebibliotheque),
    #path('traitementinstant/<int:id>/', views.traitementinstant),
    #path('formulaireinstant/<int:id>/', views.formulaireinstant)

]