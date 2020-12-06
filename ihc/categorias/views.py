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
        return redirect("/")
    else:
        return render(request,"categoriasForm.html")