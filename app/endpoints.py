from django.urls import path

from . import api

urlpatterns = [
    path('', api.routes, name='routes'),
    path('lojas', api.get_lojas, name='get_lojas'),
    path('items', api.get_items, name='get_items'),
    path('loja/<str:pk>', api.get_items_loja, name='get_items_loja'),
    path('authenticate', api.autenticar, name='authenticate'),
    path('logout', api.logout, name='logout'),
    path('criar/loja', api.create_loja, name='create_loja'),
    path('criar/item', api.create_item, name='create_item'),
    path('criar/loja_item', api.create_loja_item, name='create_loja_item'),
    path('delete/loja', api.delete_loja, name='delete_loja'),
]