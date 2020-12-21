from django.shortcuts import render, redirect
from articulos.models import Articulo,Categoria 
from salidas.models import Presentacion,Salida_Cabecera
from django.contrib import messages
from .models import Salida_Detalle

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
        disponible = False
        if ArtSitAct=="on":
            disponible = True
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
        return redirect("/articulos/listaArticulo")
    else:
        categorias = Categoria.objects.all()
        return render(request,"articuloForm.html" , context={"categorias":categorias})

    
def registrarCompra(request):
    if request.method == "POST":
        #Salida cabecera
        CabCod = request.POST["sal_det_cab_cod"]

        #Articulo
        ArtCod = request.POST["sal_det_art_cod"]

        #Unidad
        PreCod = request.POST["sal_det_pre_cod"];

        #Datos
        SalDetCabCod = Salida_Cabecera.objects.get(pk=CabCod)
        SalDetArtCod = Articulo.objects.get(pk=ArtCod)
        SalDetPreCod = Presentacion.objects.get(pk=PreCod)
        SalDetCosUni = request.POST["sal_det_cos_uni"]
        SalDetCan = request.POST["sal_det_can"]

        #Tomamos la categoria segun el ID que se recibe
        salida = Salida_Detalle.objects.create(
            SalDetCabCod=SalDetCabCod,
            SalDetArtCod=SalDetArtCod,
            SalDetPreCod=SalDetPreCod,
            SalDetCosUni=SalDetCosUni,
            SalDetCan=SalDetCan,
        )

        salida.save()
        return redirect("/articulos")
    else:
        articulos = Articulo.objects.all()
        presentaciones = Presentacion.objects.all()
        pedidos = Salida_Cabecera.objects.all()

        return render(request,"salidaDetalle.html" , context = {"pedidos":pedidos,"articulos":articulos, "presentaciones":presentaciones})


def listaArticulo(request):
    articulos = Articulo.objects.all()
    return render(request , "listaArticulos.html" , context={"articulos":articulos})

def listaCompra(request):
    compras = Salida_Detalle.objects.all()
    return render(request , "listaCompra.html" , context={"compras":compras})

