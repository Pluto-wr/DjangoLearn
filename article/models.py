from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# 创建应用模型，即设置数据库字段，模型创建完成中使用命令迁移数据库生成表数据


class Article(models.Model):
    title = models.CharField(max_length=30)  # 字符传字段，限制最长字符==30
    content = models.TextField()  # 文本字段
    objects = models.Manager()  # 加上这句才能应用objects
    created_time = models.DateTimeField(auto_now_add=True)  # 创建时间字段，设置为在添加时自动添加当前时间
    last_updated_time = models.DateTimeField(auto_now=True)  # 最后更新时间字段，设置为当前时间
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)  # 作者字段外键，关联User表。on_delete为删除时不做操作，1为超级管理用户
    is_deleted = models.BooleanField(default=False)  # 此字段标识此数据是否删除，默认为false未删除
    readed_num = models.IntegerField(default=0)  # 阅读字段


    def __str__(self):
        return '<Artqicle: %s>' % self.title