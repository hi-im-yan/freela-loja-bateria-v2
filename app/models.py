from django.db import models

# Create your models here.
class Loja(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=156)
    endereco = models.CharField(max_length=156)
    telefone = models.CharField(max_length=16)
    image = models.FileField(blank=True, null=True)

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=64)
    image = models.FileField(blank=True, null=True)

class Loja_Item(models.Model):
    id = models.AutoField(primary_key=True)
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    preco = models.FloatField()

