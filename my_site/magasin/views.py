from django.shortcuts import render ,redirect
from django.http import HttpResponseRedirect 
from .models import *
from .forms import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from django.contrib.auth import login, authenticate
from django.contrib import messages
from rest_framework.generics import ListAPIView
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
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
@login_required
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

@login_required
def filtre_categorie(request, id):
    
    categories = Categorie.objects.all()
    category = Categorie.objects.get(id=id)
    products = Produit.objects.filter(categorie=category)
    
    return render(request, 'magasin/mesProduits.html', {'products': products ,'cat':categories,'cat_filtre': category})
@login_required
def Vitrine(request):
    list=Produit.objects.all() 
    return render(request,'magasin/vitrine.html',{'list':list})

# def register(request):
#     if request.method == 'POST' :
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             login(request,user)
#             messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
#             return redirect('home')
#         else :
#             form = UserCreationForm()
#         return render(request,'register.html',{'form' : form})


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
    

# class ProductViewset(viewsets.ReadOnlyModelViewSet):

#     serializer_class = ProductSerializer
#     def get_queryset(self):
#         queryset = Produit.objects.all()
#         category_id = self.request.GET.get('category_id')
#         if category_id:
#                 queryset = queryset.filter(categorie_id=category_id)
#         return queryset


    