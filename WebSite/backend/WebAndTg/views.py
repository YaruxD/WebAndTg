from django.shortcuts import render
from .models import Catalog
from rest_framework import generics
from serializers import CatalogSerializer, UserSerializer
from django.contrib.auth.models import User

class ListCreateCatalog(generics.ListCreateAPIView):
    queryset = Catalog.objects.all()
    serializer_class = CatalogSerializer

class ListCreateUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Create your views here.
