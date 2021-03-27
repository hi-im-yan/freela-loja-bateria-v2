from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import *


import os
import requests
# Create your views here.
def home(request):
    res = requests.get(str(os.environ.get('URL') + 'api/lojas'))
    url = str(os.environ.get('URL'))
    context = {
        'URL': url[:-1],
        'lojas' : res.json()
    }

    return render(request, 'app/home.html', context)



def items(request):
    res = requests.get(str(os.environ.get('URL') + 'api/items'))
    url = str(os.environ.get('URL'))
    context = {
        'URL': url[:-1],
        'items': res.json()
    }

    return render(request, 'app/items.html', context)


def loja_items(request, pk):
    res = requests.get(str(os.environ.get('URL') + 'api/loja/' + pk))
    url = str(os.environ.get('URL'))

    context = {
        'URL': url[:-1],
        'items_loja': res.json()
    }

    return render(request, 'app/items_loja.html', context)

def login(request):
    
    return render(request, 'app/login.html')

@login_required(login_url=os.environ.get('URL') + 'login')
def dashboard(request):

    url = str(os.environ.get('URL'))
    res = requests.get(url + 'api/lojas')

    context = {
        'URL': url[:-1],
        'loja_form': LojaForm(request.POST, request.FILES),
        'lojas': res.json()

    }
    return render(request, 'app/dashboard.html', context)