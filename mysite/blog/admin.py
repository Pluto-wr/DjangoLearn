from django.contrib import admin
from .models import BlogType, Blog

# Register your models here. 注册完模型，才能在后台管理界面显示字段


@admin.register(BlogType)
class BlogTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'type_name')


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'blog_type', 'author', 'created_time', 'last_updated_time')

