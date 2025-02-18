
from django.shortcuts import render, redirect  
from .forms import AutorForm, CategoriaForm, PublicacionForm  
from .models import Publicacion  

def crear_publicacion(request):  
    if request.method == 'POST':  
        form = PublicacionForm(request.POST)  
        if form.is_valid():  
            form.save()  
            return redirect('listar_publicaciones')  
    else:  
        form = PublicacionForm()  
    return render(request, 'crear_publicacion.html', {'form': form})  

def buscar_publicacion(request):  
    query = request.GET.get('query', '')  
    publicaciones = Publicacion.objects.filter(titulo__icontains=query)  
    return render(request, 'buscar_publicacion.html', {'publicaciones': publicaciones, 'query': query})