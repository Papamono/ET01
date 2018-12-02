from django.db import models

# Create your models here.
class Usuario(models.Model):
    password = models.CharField(max_length=40)
    username = models.CharField(max_length=40)

class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    costoPre = models.IntegerField()
    costoReal = models.IntegerField()
    tienda = models.CharField(max_length=40)
    notas = models.CharField(max_length=40)

class Lista(models.Model):
    totalProdADD = models.IntegerField() #total productos agregados
    totalProdComp = models.IntegerField() #total productos comprados
    cost_presu = models.IntegerField() #costo total presupuestado
    ctotal_comp = models.IntegerField() #costo total real de los productos comprados

class Tienda(models.Model):
    nombre = models.CharField(max_length=40)
    nsucursal = models.CharField(max_length=50)
    dirección = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    región = models.CharField(max_length=100)

