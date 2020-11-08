from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation
from ckeditor_uploader.fields import RichTextUploadingField
from read_statistics.models import ReadNumExpandMethod, ReadDetail
from django.db.models.fields import exceptions
from django.contrib.contenttypes.models import ContentType
# Create your models here.


class BlogType(models.Model):
    type_name = models.CharField(max_length=15)
    objects = models.Manager()  # 加上这句才能应用objects

    def __str__(self):
        return self.type_name

    def blog_count(self):
        return self.blog_set.count()  # blog_set是反向获取被关联外键的model。模型名称小写加_set，count获取数量，相当于sql跨表查询


class Blog(models.Model, ReadNumExpandMethod):
    title = models.CharField(max_length=50)
    blog_type = models.ForeignKey(BlogType, on_delete=models.DO_NOTHING)
    content = RichTextUploadingField()
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
    created_time = models.DateTimeField(auto_now_add=True)
    last_updated_time = models.DateTimeField(auto_now=True)
    read_details = GenericRelation(ReadDetail)  # 反向通用关系，创建一个从相关对象到该对象的关系， 这里关联到ReadDetail-->Blog
    objects = models.Manager()

    def __str__(self):
        return "<Blog: %s>" % self.title

    class Meta:
        ordering = ['-created_time']  # 倒序显示列表

