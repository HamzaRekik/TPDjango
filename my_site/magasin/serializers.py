from rest_framework.serializers import ModelSerializer
from .models import *

class CategorySerializer(ModelSerializer):
    class Meta:
        model = Categorie
        fields =  '__all__'

class ProductSerializer(ModelSerializer):
    class Meta:
        model= Produit
        fields= '__all__'