from django.contrib import admin
from .models import Post, Category, Tag
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.site_header = "言念 blog 后台登陆"
admin.site.site_titler = "言念"
# Register your models here.

