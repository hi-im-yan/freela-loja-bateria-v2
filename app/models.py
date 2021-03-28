from django.db import models

# Create your models here.
class Loja(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=156)
    endereco = models.CharField(max_length=156)
    telefone = models.CharField(max_length=16)
    image = models.FileField(blank=True, null=True)
    ativo = models.IntegerField()

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=64)
    image = models.FileField(blank=True, null=True)
    ativo = models.IntegerField()

class Loja_Item(models.Model):
    id = models.AutoField(primary_key=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True)
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE, null=True)
    preco = models.FloatField()
    loja_item_ativo = models.IntegerField()

