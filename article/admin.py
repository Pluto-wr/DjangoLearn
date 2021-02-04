from django.contrib import admin
from . models import Article

# Register your models here.
# 如何在后台管理中显示APP，需要在这里注册模型


@admin.register(Article)  # 后台管理定制
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "content", "author", "is_deleted", "created_time", "last_updated_time")  # 列表显示
    ordering = ("-id", )  # 排序 -为倒叙


# admin.site.register(Article, ArticleAdmin)