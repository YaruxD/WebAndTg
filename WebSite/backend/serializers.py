from rest_framework import serializers
from WebAndTg.models import Catalog


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ['id', 'Type', 'Product', 'Description', 'Photo', 'Price']

    def create(validated_data):
        catalog = Catalog.objects.create(**validated_data)
        return catalog

