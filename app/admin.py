from django.contrib import admin
from .models import *
# Register your models here.

def getFieldsModel(model):
    return [field.name for field in model._meta.get_fields()]

class LojaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'endereco', 'telefone', 'ativo')

class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'ativo')

class Loja_ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'loja', 'item', 'preco', 'loja_item_ativo')


    
admin.site.register(Loja, LojaAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Loja_Item, Loja_ItemAdmin)