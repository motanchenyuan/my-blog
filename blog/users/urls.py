from django.conf.urls import url, include
from . import views
from django.contrib import admin

from users import views

app_name = 'users'
urlpatterns = [
    url(r'^register/', views.register, name='register'),
     url(r'^admin/', admin.site.urls),
    # 别忘记在顶部引入 include 函数
    url(r'^users/', include('users.urls')),
    url(r'^users/', include('django.contrib.auth.urls')),
    # 别忘记在顶部引入 views 模块
    url(r'^$', views.index, name='index')
        ]
