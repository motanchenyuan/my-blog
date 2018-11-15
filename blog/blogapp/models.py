# encoding:utf8
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible

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
@python_2_unicode_compatible
class Category(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Tag(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):                 
		return self.name


@python_2_unicode_compatible
class Post(models.Model):
	title = models.CharField(max_length=70)
	views = models.PositiveIntegerField(default=0) #定义阅读次数
	body = models.TextField()
	create_time = models.DateTimeField()
	modeified_time = models.DateTimeField()
	excerpt = models.CharField(max_length= 200,blank = True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	tags = models.ManyToManyField(Tag,blank=True)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	def __str__(self):                 
		return self.title
	def get_absolute_url(self):
        	return reverse('blogapp:detail', kwargs={'pk': self.pk})
	#定义阅读次数累计方法
	def increase_views(self):
        	self.views += 1
        	self.save(update_fields=['views'])


    # 自定义 get_absolute_url 方法
    # 记得从 django.urls 中导入 reverse 函数
    	

	
	
