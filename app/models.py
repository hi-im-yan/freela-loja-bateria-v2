from django.db import models

# Create your models here.
class Loja(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=64)
    endereco = models.CharField(max_length=256)
    telefone = models.IntegerField(max_length=9)
    image = models.FileField()

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=64)
    image = models.FileField()

class Loja_Item(models.Model):
    id = models.AutoField(primary_key=True)
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    preco = models.FloatField()

class Administrador(models.Model):
    id = models.AutoField(primary_key=True)
    usuario = models.CharField(max_length=124)
    senha = models.CharField(max_length=124)
