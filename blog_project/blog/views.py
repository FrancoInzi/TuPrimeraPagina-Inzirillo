from django.shortcuts import render

# Create your views here.

# blog/views.py  
from django.shortcuts import render, redirect  
from .models import Author, Post, Comment  
from .forms import AuthorForm, PostForm, CommentForm  

def home(request):  
    posts = Post.objects.all()  
    return render(request, 'blog/home.html', {'posts': posts})  

def add_author(request):  
    if request.method == 'POST':  
        form = AuthorForm(request.POST)  
        if form.is_valid():  
            form.save()  
            return redirect('home')  
    else:  
        form = AuthorForm()  
    return render(request, 'blog/add_author.html', {'form': form})  

def search(request):  
    query = request.GET.get('q')  
    results = Post.objects.filter(title__icontains=query) if query else []  
    return render(request, 'blog/search.html', {'results': results})