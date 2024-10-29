from django.shortcuts import render
from .models import Catalog
from rest_framework import generics
from serializers import CatalogSerializer

class ListCreateCatalog(generics.ListCreateAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer


# Create your views here.
