#from django.urls import path
#from . import views

#urlpatterns = [
 #   path('',view=views.index),
#]

from django.urls import path
from .views import produit_list_create

urlpatterns = [
    
    path('produits/', produit_list_create, name='produit-list-create'),
]
