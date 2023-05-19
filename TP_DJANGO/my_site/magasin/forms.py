from django import forms
from .models import *

class ProduitForm(forms.ModelForm):   
    class Meta:
        model = Produit
        fields = '__all__'

class FournisseurForm(forms.ModelForm):   
    class Meta:
        model = Fournisseur
        fields = '__all__'
