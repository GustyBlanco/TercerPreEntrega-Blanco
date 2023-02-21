from django.db import models

# Create your models here.

class Kinesiologos(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    comision=models.IntegerField()
    mail=models.EmailField()
    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido:{self.apellido} - Comision: {self.comision} - Mail: {self.mail}'
class Masajistas(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    credencial=models.IntegerField()
    interno=models.IntegerField()
    
    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - N°Credencial: {self.credencial} - Interno: {self.interno}'
class Proyecto(models.Model):
    nombre= models.CharField(max_length=30)
    fechaDeEntrega= models.DateField()
    entregado= models.BooleanField()
    
    def __str__(self):
        return f"Nombre: {self.nombre} - fecha de entrega: {self.fechaDeEntrega} - Estado: {self.entregado}"