import markdown
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post,Category
from django.shortcuts import render, get_object_or_404
'''from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()
'''
def index(request):
	post_list = Post.objects.all().order_by('-create_time')
	return render(request,'blog/index.html',context={
	#	'title':'welcom to my blog',
	#	'welcome':'welcom to my blog index',
		'post_list':post_list,

	})
def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions = [
				  'markdown.extensions.extra',
				  'markdown.extensions.codehilite',
				  'markdown.extensions.toc',
				  ])
    return render(request, 'blog/detail.html', context={'post': post})
def archives(request,year,month):
    post_list = Post.objects.filter(create_time__year=year,
				    create_time__month=month,
					).order_by('-create_time')
    return render(request,'blog/index.html',context={'post_list': post_list})
def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list': post_list })

