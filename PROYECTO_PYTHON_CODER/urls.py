
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path("", include("inicio.urls")),
    path("categorias/", include("categorias.urls")),
    path("usuarios/", include("usuarios.urls")),

   

    

]
