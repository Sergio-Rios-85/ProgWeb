from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre=models.CharField(max_length=30)
    diereccion=models.CharField(max_length=50)
    email=models.EmailField(blank=True, null=True)
    celular=models.CharField(max_length=9)

    def __str__(self):
        return ' %s' %(self.nombre)

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()   

    def __str__(self):
        return 'El nombre es %s la seccion es %s y el valor es %s' %(self.nombre,self.seccion,self.precio)                                                                                  

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()    
 