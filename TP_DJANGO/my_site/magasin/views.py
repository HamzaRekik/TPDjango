from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
# Create your views here.

def index(request):
    products= Produit.objects.all()
    categories = Categorie.objects.all()    
    if request.method == "POST" : 
        form = ProduitForm(request.POST,request.FILES) 
        if form.is_valid(): 
            form.save() 
        return HttpResponseRedirect('/magasin') 
    else : form = ProduitForm()
    context={'products':products,'cat':categories,'form':form}
    return render(request,'magasin/mesProduits.html',context)

def fourniseur(request):
    fourniseurs = Fournisseur.objects.all()
    categories = Categorie.objects.all()
    if request.method == "POST" : 
        form = FournisseurForm(request.POST,request.FILES) 
        if form.is_valid(): 
            form.save() 
        return HttpResponseRedirect('/magasin/fourniseurs') 
    else : form = FournisseurForm()
    context = {'fourniseurs' : fourniseurs ,'cat':categories,'form':form}
    return render(request,'magasin/fourniseurs.html',context)


def filtre_categorie(request, id):
    
    categories = Categorie.objects.all()
    category = Categorie.objects.get(id=id)
    products = Produit.objects.filter(categorie=category)
    
    return render(request, 'magasin/mesProduits.html', {'products': products ,'cat':categories,'cat_filtre': category})

def Vitrine(request):
    list=Produit.objects.all() 
    return render(request,'magasin/vitrine.html',{'list':list})

class CategoryAPIView(APIView):
    def get(self,*args,**kwargs):
        categoriers = Categorie.objects.all()
        serializer = CategorySerializer(categoriers,many=True)
        return Response(serializer.data)
    
class ProductAPIView(APIView):
    def get(self,*args, **kwargs):
        produits = Produit.objects.all()
        serializer = ProductSerializer(produits,many=True)
        return Response(serializer.data)
    
class ProductViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    def get_queryset(self):
        queryset = Produit.objects.all()
        categorie_id = self.request.GET.get('categorie_id')
        if categorie_id : 
            queryset = queryset.filter(categorie=categorie_id)
        return queryset


    