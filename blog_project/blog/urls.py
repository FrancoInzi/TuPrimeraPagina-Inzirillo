# blog/urls.py  
from django.urls import path  
from .views import home, add_author, search  

urlpatterns = [  
    path('', home, name='home'),  
    path('add_author/', add_author, name='add_author'),  
    path('search/', search, name='search'),  
]

# blog_project/urls.py  
from django.contrib import admin  
from django.urls import path, include  

urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('', include('blog.urls')),  
]