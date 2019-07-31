# encoding:utf8
from django.db import models
from django.conf import settings #setting 中User

from django.contrib import admin
#from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible
#from django.contrib.auth.models import AbstractUser

class Blog(models.Model):
 #博客(个人站点)信息

    nid = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name='个人博客标题', max_length=64)
    site = models.CharField(verbose_name='个人博客后缀', max_length=32, unique=True)
    theme = models.CharField(verbose_name='博客主题', max_length=32)
    def __str__(self):
        return self.title


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
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	def __str__(self):                 
		return self.title
	def get_absolute_url(self):
        	return reverse('blogapp:detail', kwargs={'pk': self.pk})
	#定义阅读次数累计方法
	def increase_views(self):
        	self.views += 1
        	self.save(update_fields=['views'])

