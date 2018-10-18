from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Post
def index(request):
	post_list = Post.objects.all().order_by('-create_time')
	return render(request,'blog/index.html',context={
		'title':'welcom to my blog',
		'welcome':'welcom to my blog index',
		'post_list':post_list,

	})
