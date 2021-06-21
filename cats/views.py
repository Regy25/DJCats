from django.shortcuts import render, redirect, get_object_or_404
from .models import Cats
from .forms import CatsForm


def listar_cats(request):
    # queryset   ..... SELECT * FROM CATS
    cats = Cats.objects.all()
    return render(request, "cats/listar_cats.html", {'cats': cats})

# Create your views here.
# def add_cat(request):
#     if request.method == "POST":
#         form = CatsForm(request.POST, files=request.FILES)
#         if form.is_valid():
#             model_instance = form.save(commit=False)
#             model_instance.save()
#             return redirect("/add_cat")
#     else:
#         form = CatsForm()
#     return render(request, "cats/add_cat.html", {'form': form})

def add_cat(request):
    
    data={
        'form' : CatsForm()
    }
    
    if request.method == 'POST':
        formulario = CatsForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario
    return render(request, "cats/add_cat.html", data) 

def borrar_cat(request, id_cat):
    # Recuperamos la instancia de los CATS y la borramos
    instancia = Cats.objects.get(id=id_cat)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('listar_cats')

def editar_cat(request, id_cat):
    cat = get_object_or_404(Cats, id=id_cat)
    
    data = {
        'form' : CatsForm(instance=cat)
    }
    
    if request.method == 'POST':
        formulario = CatsForm(data=request.POST, instance=cat, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect (to="listar_cats")
        data["form"] = formulario
         
    return render(request, "cats/editar_cat.html", data)

def home(request):
    return render(request, "cats/home.html")