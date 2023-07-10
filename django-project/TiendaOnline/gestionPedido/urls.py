from django.urls import path

from gestionPedido import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   
    path('busqueda_producto/', views.busqueda_productos, name="Busqueda"),
    path('buscar/', views.buscar, name="Buscar"),
    path('contacto/', views.contacto, name="Contacto"),
    path('', views.index, name="index"),
    path('anillo/', views.anillo, name="anillo"),
    path('cuadro/', views.cuadro, name="cuadro"),
    path('estatua/', views.estatua, name="estatua"),
    path('nosotros/', views.nosotros, name="nosotros"),

]
  
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  