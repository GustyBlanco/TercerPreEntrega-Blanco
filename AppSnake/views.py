from django.shortcuts import render
from django.http import HttpResponse
from AppSnake.models import *

#from django.http import HttpResponse
from AppSnake.forms import form_masajistas,form_kinesiologos, form_proyecto
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

def inicio(request):
    
    return render(request,'AppSnake/Inicio.html')


def masajista(request):
    masajista= Masajistas.objects.all()
    contexto= {"masajista":Masajistas}
    return render(request,'AppSnake/masajistas.html',contexto)

def proyecto(request):

    return render(request,'AppSnake/Proyecto.html')

def masajistaFormulario(request):
    if request.method == "POST":
        miFormulario=form_masajistas(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            masajista= Masajistas(nombre=informacion['nombre'],credencial=informacion['credencial'],apellido= informacion['apellido'],interno= informacion['interno'])
            masajista.save()
            return render(request,'AppSnake/inicio.html') 
    else:
        miFormulario=form_masajistas()
    return render(request,'AppSnake/masajistaFormulario.html',{'miFormulario':miFormulario})

def masajistaBusqueda(request):
    return render(request,'AppSnake/masajistaBusqueda.html',{"masajista":masajista})

def buscar(request):
    if request.GET["credencial"]:

        credencial=request.GET["credencial"]
        masajista=Masajistas.objects.filter(credencial__icontains=credencial)

        return render(request,"AppSnake/resultadoBusqueda.html",{"masajistas":masajista,"credencial":credencial})
    else:
        respuesta='No enviaste datos'
       
    return HttpResponse(respuesta)

def kinesiologo(request):
    kinesiologo= Kinesiologos.objects.all()
    contexto= {"kinesiologo":Kinesiologos}
    return render(request,'AppSnake/kinesiologos.html',contexto)
 
def kinesiologoFormulario(request):
    if request.method == "POST":
        miFormulario=form_kinesiologos(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion=miFormulario.cleaned_data
            kinesiologo= Kinesiologos(nombre=informacion['nombre'],comision=informacion['comision'],apellido= informacion['apellido'],mail=informacion['mail'])
            kinesiologo.save()
            return render(request,'AppSnake/inicio.html') 
    else:
        miFormulario=form_kinesiologos()
    return render(request,'AppSnake/kinesiologoFormulario.html',{'miFormulario':miFormulario})

def kinesiologoBusqueda(request):
    return render(request,'AppSnake/kinesiologoBusqueda.html',{"kinesiologo":kinesiologo})

def buscar2(request):
    if request.GET["apellido"]:

        apellido=request.GET["apellido"]
        kinesiologo=Kinesiologos.objects.filter(apellido__icontains=apellido)

        return render(request,"AppSnake/resultadoBusqueda2.html",{"kinesiologos":kinesiologo,"apellido":apellido})
    else:
        respuesta='No enviaste datos'
       
    return HttpResponse(respuesta)

def proyectoFormulario(request):
    story=Proyecto.objects.all()

    context={
        'stories':story,
    }

    return render(request,"AppSnake/proyectoFormulario.html",context)