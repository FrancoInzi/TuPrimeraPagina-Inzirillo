 
from django import forms  
from .models import Autor, Categoria, Publicacion  

class AutorForm(forms.ModelForm):  
    class Meta:  
        model = Autor  
        fields = ['nombre', 'email']  

class CategoriaForm(forms.ModelForm):  
    class Meta:  
        model = Categoria  
        fields = ['nombre']  

class PublicacionForm(forms.ModelForm):  
    class Meta:  
        model = Publicacion  
        fields = ['titulo', 'contenido', 'autor', 'categoria']  