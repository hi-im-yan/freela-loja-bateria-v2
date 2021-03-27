from rest_framework import serializers
from .models import *

class LojaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loja
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
        
class Loja_ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loja_Item
        fields = '__all__'
