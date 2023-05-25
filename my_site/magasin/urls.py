from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('',views.index , name='index'),
    path('fourniseurs',views.fourniseur ,name='fourniseurs'),
    path('<int:id>/',views.filtre_categorie, name='produit_par_cat'),
    path('vitrine',views.Vitrine),
    path('api/category/',CategoryAPIView.as_view()),
    path('api/product/',ProductAPIView.as_view()),
   
   

]
