from django.shortcuts import render, redirect
from .models import Categoria
from django.contrib import messages
# Create your views here.

def registroCategoria(request):
    if request.method == "POST":
        CatCod = request.POST["cat_cod"]
        CatDes = request.POST["cat_des"]
        #CatImg = request.POST["cat_img"]

        categoria = Categoria.objects.create(
            CatCod = CatCod,
            CatDes = CatDes,
            #CatImg = CatImg
        )
        categoria.save();
        print("Se ha creado la nueva categoria");
        return redirect("/categorias/mostrarCategoria")
    else:
        return render(request,"categoriasForm.html")

def mostrarCategoria(request):
    categorias = Categoria.objects.all();
    return render(request,"categoriasMostrar.html" , context={"categorias":categorias})

def actualizarCategoria(request , id):
    categoria = Categoria.objects.get(pk=id);
    if(request.method == "POST" or None):
        CatCod = request.POST["cat_cod"]
        CatDes = request.POST["cat_des"]
        categoria.CatCod = CatCod
        categoria.CatDes = CatDes
        categoria.save()
        return redirect("/categorias/mostrarCategoria")
    return render(request , "categoriasUpdate.html" , context={"categoria":categoria})

def eliminarCategoria(request , id):
    eliminado = Categoria.objects.get(pk=id)
    if eliminado != None:
        eliminado.delete()
    return redirect("/categorias/mostrarCategoria");

def categoriaHome(request):
    return render(request , "categorias.html")