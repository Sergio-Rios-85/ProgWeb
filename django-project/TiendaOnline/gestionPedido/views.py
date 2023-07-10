from django.shortcuts import render
from django.http import HttpResponse
from gestionPedido.models import Articulos
from django.core.mail import send_mail
from django.conf import settings
from gestionPedido.forms import FormularioContacto
from servicios.models import Servicio
 
 

# Create your views here.
 
def busqueda_productos(request):
    return render(request,"gestionPedido/busqueda_producto.html") 

def buscar(request):

    if request.GET["prd"]:
        #mensaje="Articulo buscado: %r" %request.GET["prd"
        producto=request.GET["prd"]

        if len(producto)>20:
            mensaje="Texto demasiado largo"
        else:
         
            articulos=Articulos.objects.filter(nombre__icontains=producto)

            return render(request, "gestionPedido/resultados_busqueda.html", {"articulos":articulos, "query":producto})

    else:
        mensaje="No haz introducido nada"    

    return HttpResponse(mensaje)

#def contacto(request):
    if request.method=="POST":
        subject=request.POST["asunto"]
        message=request.POST["mensaje"] + " " + request.POST["email"]
        email_from=settings.EMAIL_HOST_USER
        recipient_list=["2012sergiorios@gmail.com"]
        send_mail(subject, message, email_from, recipient_list)

        return render(request, "gracias.html")
    return render(request, "contacto.html")

def contacto(request):
    if request.method=="POST":
        miFormulario=FormularioContacto(request.POST)

        if miFormulario.is_valid():
            infForm=miFormulario.cleaned_data

            send_mail(infForm['asunto'], infForm['mensaje'], infForm.get('email',''),['2012sergiorios@gmail.com'],)

            return render(request, "gestionPedido/gracias.html")

    else:
        miFormulario=FormularioContacto()

    return render(request, "gestionPedido/formulario_contacto.html", {"form":miFormulario})      


def index(request):
    return render(request,"gestionPedido/index.html")

def anillo(request):
    return render(request,"gestionPedido/anillo.html")

def estatua(request):
    return render(request,"gestionPedido/estatua.html")

def cuadro(request):
    return render(request,"gestionPedido/cuadro.html")

def nosotros(request):
    return render(request,"gestionPedido/nosotros.html")

def servicios(request):
    servicios=Servicio.objects.all()
    return render(request,"gestionPedido/servicios.html", {"servicios":servicios})