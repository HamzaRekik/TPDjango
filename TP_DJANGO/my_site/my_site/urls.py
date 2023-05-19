from django.contrib import admin
from django.urls import path,include
from django.conf import settings 
from django.conf.urls.static import static
from django.contrib import admin, auth
from django.contrib.auth import views as auth_views
from . import views
from rest_framework import routers
from magasin.views import *

router = routers.SimpleRouter()
router.register('produit',ProductViewset,basename='produit')
urlpatterns = [
    path('',views.main),
    path('admin/', admin.site.urls),
    path('magasin/',include('magasin.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name = 'logout'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'), name = 'login'),
    path('register/',views.register, name = 'register'),
    path('api_auth/',include('rest_framework.urls')),
    path('api/',include(router.urls))
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
