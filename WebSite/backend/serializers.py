from rest_framework import serializers
from WebAndTg.models import Catalog
from django.contrib.auth.models import User


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ['id', 'Type', 'Product', 'Description', 'Photo', 'Price']

    def create(self, validated_data):
        catalog = Catalog.objects.create(**validated_data)
        return catalog

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(serlf, validated_data):
        user = User.objects.create_user(**validated_data)
        return user