from django.shortcuts import render,redirect
from .models import Cats
from .forms import CatsForm


def listar_cats(request):
    # queryset   ..... SELECT * FROM CATS
    cats = Cats.objects.all()
    return render(request, "cats/listar_cats.html", {'cats': cats})

# Create your views here.
def add_cat(request):
    if request.method == "POST":
        form = CatsForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect("/add_cat")
    else:
        form = CatsForm()
        return render(request, "cats/add_cat.html", {'form': form})

def borrar_cat(request, id_cat):
    # Recuperamos la instancia de los CATS y la borramos
    instancia = Cats.objects.get(id=id_cat)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('listar_cats')

def editar_cat(request, id_cat):
    # Recuperamos la instancia de los CATS
    instancia = Cats.objects.get(id=id_cat)

    # Creamos el formulario con los datos de la instancia
    form = CatsForm(instance=instancia)

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = CatsForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manipular antes de grabar
            instancia = form.save(commit=False)
            # Podemos guardar cuando queramos
            instancia.save()

    # Si llegamos al final renderizamos el formulario
    return render(request, "cats/editar_cat.html", {'form': form})

def home(request):
    return render(request, "cats/home.html")