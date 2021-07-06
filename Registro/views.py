from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cats
from .forms import CatsForm
from django.contrib.auth import logout
# las importaciones para la API 
from rest_framework import generics
from .serializers import CatsSerializer
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status


# Create your views here.

def listar_cats(request):
    cats = Cats.objects.all()
    return render(request, "cats/listar_cats.html", {'cats': cats})

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

@login_required(login_url='/admin/')
def borrar_cat(request, id_cat):
    instancia = Cats.objects.get(id=id_cat)
    instancia.delete()
    return redirect('listar_cats')

@login_required(login_url='/admin/')
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

def redir_home(request):
    return redirect('home')


def logout_view(request):
    logout(request)
    return redirect('home')

#api

@api_view(['GET', 'POST'])
def cat_collection(request):
    if request.method == 'GET':
        cat = Cats.objects.all()
        serializer = CatsSerializer(cat, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CatsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def cat_element(request, pk):
    cat = get_object_or_404(Cats, id=pk)

    if request.method == 'GET':
        serializer = CatsSerializer(cat)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        cat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT': 
        cat_new = JSONParser().parse(request) 
        serializer = CatsSerializer(cat, data=cat_new) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


