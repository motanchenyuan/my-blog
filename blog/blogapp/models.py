# encoding:utf8
from django.db import models
from django.contrib import admin


class Article(models.Model):
    title = models.CharField(max_length=100)    
    category = models.TextField(max_length=50, blank=True)  
    date_time = models.DateTimeField(auto_now_add=True) 
    content = models.TextField(blank=True, null = True) 

    def __unicode__(self):
        return self.title

    class Meta: 
        ordering = ['-date_time']

# Register model
admin.site.register(Article)
