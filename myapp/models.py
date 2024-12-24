from django.db import models

class BlogModel(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=300)
    date = models.DateField(auto_now_add=True)
    message = models.TextField(null=True, blank=True)  

