from django.db import models

class Cliente(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField(blank=True, null=True)
    celular=models.CharField(max_length=9)

    def __str__(self):
        return ' %s' %(self.nombre)

class Articulo(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    autor=models.CharField(max_length=20)
    precio=models.IntegerField()   

    def __str__(self):
        return 'El nombre es %s la seccion es %s autor %s y el valor es %s' %(self.nombre,self.seccion,self.autor,self.precio)                                                                                  

class Pedido(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()    


class Servicio(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to="servicios")
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True)
     
    class Meta:
        verbose_name='servicio'
        verbose_name_plural='servicios'

    def __str__(self):
        return self.titulo  
