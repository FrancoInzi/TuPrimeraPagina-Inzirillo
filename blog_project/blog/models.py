from django.db import models

# blog/models.py  
from django.db import models  

class Author(models.Model):  
    name = models.CharField(max_length=100)  
    email = models.EmailField()  

    def __str__(self):  
        return self.name  

class Post(models.Model):  
    title = models.CharField(max_length=200)  
    content = models.TextField()  
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  

    def __str__(self):  
        return self.title  

class Comment(models.Model):  
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  
    author_name = models.CharField(max_length=100)  
    text = models.TextField()  

    def __str__(self):  
        return f'{self.author_name} - {self.post.title}'
