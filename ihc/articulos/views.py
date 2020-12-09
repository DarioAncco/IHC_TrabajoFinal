from django.shortcuts import render, redirect
from articulos.models import Articulo,Categoria 
from django.contrib import messages

# Create your views here.

def registroArticulo(request):
    if request.method == "POST":
        ArtCod = request.POST["art_cod"]
        ArtNom = request.POST["art_nom"]
        ArtDes = request.POST["art_des"]
        #ArtImg = request.POST["art_img"] #Por el momento no hay tiempo!
        ArtCatCod = request.POST["art_cat_cod"]
        ArtCosUni = request.POST["art_cos_uni"]
        ArtSitAct = request.POST["art_sit_act"]
        ArtSto = request.POST["art_sto"]

        #Tomamos la categoria segun el ID que se recibe
        categoria = Categoria.objects.get(pk=ArtCatCod)
        if ArtSitAct=="on":
            disponible = True
        else:
            disponible = False;

        articulo = Articulo.objects.create(
            ArtCod=ArtCod,
            ArtNom=ArtNom,
            ArtDes=ArtDes,
            #ArtImg=ArtImg,
            ArtCatCod=categoria,
            ArtCosUni=ArtCosUni,
            ArtSitAct=disponible,
            ArtSto=ArtSto
        )
        articulo.save();
        return redirect("/")
    else:
        return render(request,"articuloForm.html")