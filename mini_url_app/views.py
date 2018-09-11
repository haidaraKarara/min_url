from django.shortcuts import render
from django.shortcuts import redirect,get_object_or_404,render

from .models import MiniURL
from .forms import MiniURLForm
# Create your views here.
def liste(request):
    """Affichage de la
        liste de redirections"""
    minis = MiniURL.objects.order_by('-nb_acces')
    return render(request,'mini_url_app/liste.html',locals())

def nouveau(request):
    """Ajout d'une redirection"""
    if request.method == "POST":
        form = MiniURLForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(liste)
    else:
        form = MiniURLForm()
    return render(request,'mini_url_app/nouveau.html',{'form':form})


def redirection(request,code):
    """Redirection vers l'url enregistrée """
    mini = get_object_or_404(MiniURL,code=code)
    mini.nb_acces +=1
    mini.save()
    return redirect(mini.url,permanent=True)
