from django.urls import path

from . import api

urlpatterns = [
    path('', api.routes, name='routes'),
    path('lojas', api.get_lojas, name='get_lojas'),
    path('items', api.get_items, name='get_items'),
    path('loja/<str:pk>', api.get_items_loja, name='get_items_loja'),
    path('authenticate', api.autenticar, name='authenticate'),
    path('logout', api.logout, name='logout'),
    
    path('criar/item', api.create_item, name='create_item'),
    path('delete/item', api.delete_item, name='delete_item'),
    path('edit/item', api.edit_item, name='edit_item'),

    path('criar/loja', api.create_loja, name='create_loja'),
    path('delete/loja', api.delete_loja, name='delete_loja'),
    path('edit/loja', api.edit_loja, name='edit_loja'),

    path('criar/loja_item', api.create_loja_item, name='create_loja_item'),
    path('delete/loja_item', api.delete_loja_item, name='delete_loja'),
    path('edit/loja_item', api.edit_loja_item, name='edit_loja_item'),
]