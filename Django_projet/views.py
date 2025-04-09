#from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.

#def index(request) -> HttpResponse :
 #   return HttpResponse("Hello world!")

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Produit
from .serializers import ProduitSerializer

@api_view(['GET', 'POST'])
def produit_list_create(request):
    if request.method == 'GET':
        produits = Produit.objects.all()
        serializer = ProduitSerializer(produits, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProduitSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

