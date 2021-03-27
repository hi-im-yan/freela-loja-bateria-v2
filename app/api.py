from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.http import JsonResponse
# from django.contrib import messages
from django.conf import settings
# from django.core.files.storage import FileSystemStorage

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import *
from .models import *

import os
import json

@api_view(['GET'])
def routes(request):
    context = {
        'teste': 'teste'
    }

    return Response(context)

@api_view(['GET'])
def get_lojas(request):
    lojas = Loja.objects.all()
    serializer = LojaSerializer(instance=lojas, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_items(request):
    items = Item.objects.all()
    serializer = ItemSerializer(instance=items, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def get_items_loja(request, pk):
    loja = Loja.objects.get(id=pk)
    loja_serializer = LojaSerializer(instance=loja, many=False)
    
    items_loja = Loja_Item.objects.filter(loja=loja)
    items_loja_serializer = Loja_ItemSerializer(instance=items_loja, many=True)

    list_items_loja = []
    for item in items_loja_serializer.data:
        temp_item = Item.objects.get(id=item['item'])
        temp_item_serializer = ItemSerializer(instance=temp_item, many=False)
        dict = {
            'nome' : temp_item_serializer.data['nome'],
            'image' : temp_item_serializer.data['image'],
            'preco': item['preco']
        }
        list_items_loja.append(dict)

    context = {
        'loja' : loja_serializer.data,
        'items' : list_items_loja
    }
    return Response(context)

def autenticar(request):
    if(request.method == 'POST'):
        form_result = request.body.decode('utf-8')
        form_result = json.loads(form_result)
        user = authenticate(request, username=form_result['usuario'], password=form_result['senha'])
        if user is not None:
            login(request, user)
            response = {
                'status': 200,
                'message': 'Autorizado'
            }
            return JsonResponse(response)
        else:
            logout(request)
            return JsonResponse({'status': 403, 'message': 'Usuário ou senha inválida'})
    else:
        pass

def logout(request):
    return redirect(os.environ.get('URL'))

@login_required(login_url=os.environ.get('URL') + 'login')
@api_view(['POST'])
def create_loja(request):

    myfile = request.FILES['image']
    fs = FileSystemStorage()
    filename = fs.save(str(myfile), myfile)
    uploaded_file_url = fs.url(filename)

    info_data = {
        'nome': request.data.get('nome'),
        'endereco': request.data.get('endereco'),
        'telefone': request.data.get('telefone')
    }
    

    serializer = LojaSerializer(data=info_data)
    if serializer.is_valid():
        serializer.save(image=request.FILES['image'])
        return redirect(os.environ.get('URL') + 'dashboard')


    return Response(info_data)

@login_required(login_url=os.environ.get('URL') + 'login')
@api_view(['POST'])
def create_item(request):
    print(request.data)
    return Response(request.data)


@login_required(login_url=os.environ.get('URL') + 'login')
@api_view(['POST'])
def create_loja_item(request):
    print(request.data)
    return Response(request.data)

@login_required(login_url=os.environ.get('URL') + 'login')
@api_view(['POST'])
def delete_loja(request):
    print(request.data.get('loja_id'))
    Loja.objects.filter(pk=request.data.get('loja_id')).delete()
    return redirect(os.environ.get('URL') + 'dashboard')