from django.shortcuts import render, HttpResponseRedirect
from .forms import CSGOForm, MajorForm, CSGOInstantForm
from . import models



def accueilcsgo(request):
    liste = list(models.CSGO.objects.all())
    return render(request, "csgo/accueilcsgo.html", {"liste": liste})

def formulairecsgo(request):
    if request.method == "POST":
        form = CSGOForm(request)
        return render(request, 'csgo/formulairecsgo.html', {'form': form})
    else:
        form = CSGOForm()
        return render(request, 'csgo/formulairecsgo.html', {'form': form})


def traitementcsgo(request):
    pForm = CSGOForm(request.POST)
    if pForm.is_valid():
        CSGO = pForm.save()
        return HttpResponseRedirect("/csgo/")
    else:
        return render(request, 'csgo/traitementcsgo.html', {'form': pForm})

def affichecsgo(request, id):
    CSGO = models.CSGO.objects.get(pk=id)
    return render(request, "csgo/affichecsgo.html", {"csgo": csgo})



def updatecsgo(request, id):
     CSGO = models.CSGO.objects.get(pk=id)
     form = CSGOForm(CSGO.dico())
     return render(request, "csgo/formulairecsgo.html", {"form": form, "id": id})


def updatetraitementcsgo(request, id):
     pform = CSGOForm(request.POST)
     if pform.is_valid():
         CSGO = pform.save(commit=False)
         CSGO.id = id
         CSGO.save()
         return HttpResponseRedirect("/csgo/")
     else:
         return render(request, "csgo/formulairecsgo.html", {"form": pform, "id": id})


def deletecsgo(request, id):
     CSGO = models.CSGO.objects.get(pk=id)
     CSGO.delete()
     return HttpResponseRedirect("/csgo/")

def accueilmajor(request):
        liste = list(models.Major.objects.all())
        return render(request, "csgo/accueilmajor.html", {"liste": liste})




# #def formulairebibliotheque(request):
#     if request.method == "POST":
#         form = MajorForm(request)
#         return render(request, 'Bibliotheque/formulairebibliotheque.html', {'form': form})
#     else:
#         form = MajorForm()
#         return render(request, 'Bibliotheque/formulairebibliotheque.html', {'form': form})


# #def affichebibliotheque(request, id):
#     bibli = models.Major.objects.get(pk=id)
#     liste = list(models.CSGO.objects.filter(bibliotheque_id=id)),
#     return render(request, "Bibliotheque/affichebibliotheque.html", {"Bibliotheque": bibli, "liste": liste})


# #def traitementbibliotheque(request):
#     pForm = MajorForm(request.POST)
#     if pForm.is_valid():
#         Bibliotheque = pForm.save()
#         return HttpResponseRedirect(f"/livre/affichebibliotheque/{Bibliotheque.id}/")
#     else:
#         return render(request, 'Bibliotheque/traitementbibliotheque.html', {'form': pForm})


# #def updatebibliotheque(request, id):
#     Bibliotheque = models.Major.objects.get(pk=id)
#     form = MajorForm(Bibliotheque.dico())
#     return render(request, "Bibliotheque/formulairebibliotheque.html", {"form": form, "id": id})


# #def updatetraitementbibliotheque(request, id):
#     pform = MajorForm(request.POST)
#     if pform.is_valid():
#         Bibliotheque = pform.save(commit=False)
#         Bibliotheque.id = id
#         Bibliotheque.save()
#         return HttpResponseRedirect("/livre/")
#     else:
#         return render(request, "Bibliotheque/formulairebibliotheque.html", {"form": pform, "id": id})


# #def deletebibliotheque(request, id):
#     Bibliotheque = models.Major.objects.get(pk=id)
#     Bibliotheque.delete()
#     return HttpResponseRedirect("/livre/accueil")


# #def formulaireinstant(request, id):
#     form = LivreInstantForm()
#     return render(request, 'livre/formulaireinstant.html', {'form': form, "id": id})


# #def traitementinstant(request, id):
#     if request.method == "POST":
#         pForm = LivreInstantForm(request.POST)
#         if pForm.is_valid():
#             livre = pForm.save(commit=False)
#             livre.bibliotheque_id = id
#             livre.bibliotheque = models.Bibliotheque.objects.get(pk=id)
#             livre.save()
#             return render(request, 'livre/traitementinstant.html', {'livre': livre, "id": id})
#         else:
#             return render(request, 'livre/formulaireinstant.html', {'form': pForm, "id": id})



