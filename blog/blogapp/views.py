import markdown
from django.shortcuts import render
from comments.forms import CommentForm
#注册登录
#from django.shortcuts import render, redirect
#from comments.forms import RegisterForm

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
    post.increase_views()
    post.body = markdown.markdown(post.body,
                                  extensions = [
				  'markdown.extensions.extra',
				  'markdown.extensions.codehilite',
				  'markdown.extensions.toc',
				  ])
	 # 记得在顶部导入 CommentForm
    form = CommentForm()
    # 获取这篇 post 下的全部评论
    comment_list = post.comment_set.all()

    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    
    return render(request, 'blog/detail.html',context=context)
def archives(request,year,month):
    post_list = Post.objects.filter(create_time__year=year,
				    create_time__month=month,
					).order_by('-create_time')
    return render(request,'blog/index.html',context={'post_list': post_list})
def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-create_time')
    return render(request, 'blog/index.html', context={'post_list': post_list })
def tag(request,pk):
    tags=Post.objects.tags.all()
    return render(request, 'blog/index.html',context={'tags':tags})
'''
#以下为用户登录模块
def register(request):
    # 只有当请求为 POST 时，才表示用户提交了注册信息
    if request.method == 'POST':
        # request.POST 是一个类字典数据结构，记录了用户提交的注册信息
        # 这里提交的就是用户名（username）、密码（password）、邮箱（email）
        # 用这些数据实例化一个用户注册表单
        form = RegisterForm(request.POST)

        # 验证数据的合法性
        if form.is_valid():
            # 如果提交数据合法，调用表单的 save 方法将用户数据保存到数据库
            form.save()

            # 注册成功，跳转回首页
            return redirect('/')
    else:
        # 请求不是 POST，表明用户正在访问注册页面，展示一个空的注册表单给用户
        form = RegisterForm()

    # 渲染模板
    # 如果用户正在访问注册页面，则渲染的是一个空的注册表单
    # 如果用户通过表单提交注册信息，但是数据验证不合法，则渲染的是一个带有错误信息的表单
    return render(request, 'register.html', context={'form': form})
    '''
