#!/usr/bin/env python  
import os  
import sys  

if __name__ == "__main__":  
    # Cambia 'myproject' a tu nombre de proyecto  
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.blog_project.settings')  # o el nombre de tu carpeta de configuración  

    try:  
        from django.core.management import execute_from_command_line  
    except ImportError as exc:  
        raise ImportError(  
            "Couldn't import Django. Are you sure it's installed and "  
            "available on your PYTHONPATH environment variable? Did you "  
            "forget to activate a virtual environment?"  
        ) from exc  
    execute_from_command_line(sys.argv)