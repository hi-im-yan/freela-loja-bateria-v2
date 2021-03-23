from django.urls import path

from . import api

urlpatterns = [
    path('', api.routes, name='routes'),
    path('lojas', api.get_lojas, name='get_lojas'),
    path('items', api.get_items, name='get_items'),
    path('loja/<str:pk>', api.get_items_loja, name='get_items_loja'),
    path('authenticate', api.autenticar, name='authenticate'),
    path('logout', api.logout, name='logout')
]