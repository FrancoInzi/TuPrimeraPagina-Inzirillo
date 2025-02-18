
from django.urls import path  
from .views import crear_publicacion, buscar_publicacion  

urlpatterns = [  
    path('crear/', crear_publicacion, name='crear_publicacion'),  
    path('buscar/', buscar_publicacion, name='buscar_publicacion'),  
]

