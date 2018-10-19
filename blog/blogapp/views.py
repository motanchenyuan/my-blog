from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404
'''from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()
'''
def index(request):
	post_list = Post.objects.all().order_by('-create_time')
	return render(request,'blog/index.html',context={
		'title':'welcom to my blog',
		'welcome':'welcom to my blog index',
		'post_list':post_list,

	})
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', context={'post': post})
