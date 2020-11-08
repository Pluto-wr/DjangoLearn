from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey # 外键


# Create your models here.
class Comment(models.Model):
    # 对应任何类型的字段
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)  # 多对一，外键指向ContentType模型
    object_id = models.PositiveIntegerField()  # 数值字段类型，存储将要关联的模型中的主键值
    content_object = GenericForeignKey('content_type', 'object_id')  # 特殊的字段类型,允许与任何模型建立关系

    text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ['-comment_time']
