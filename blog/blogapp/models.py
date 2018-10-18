# encoding:utf8
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

'''class Article(models.Model):
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
'''
class Category(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name
class Tag(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):                 
		return self.name
class Post(models.Model):
	title = models.CharField(max_length=70)
	def __str__(self):                 
		return self.name
	body = models.TextField()
	create_time = models.DateTimeField()
	modeified_time = models.DateTimeField()
	excerpt = models.CharField(max_length= 200,blank = True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	tags = models.ManyToManyField(Tag,blank=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	
