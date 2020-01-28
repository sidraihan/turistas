from rest_framework import serializers
from .models import Place,Category


class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("__all__")

class PlaceSerializer(serializers.ModelSerializer):

    description = DescriptionSerializer(read_only=True,many=True)
    class Meta:
        model = Place
        fields = ("name", "description","longitude","latitude")