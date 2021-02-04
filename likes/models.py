from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey # 外键
from django.contrib.auth.models import User
# Create your models here.


class LikeCount(models.Model):
    # 对应任何类型的字段
    objects = models.Manager()  # 加上这句才能应用objects
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # 多对一，外键指向ContentType模型
    object_id = models.PositiveIntegerField()  # 数值字段类型，存储将要关联的模型中的主键值
    content_object = GenericForeignKey('content_type', 'object_id')  # 特殊的字段类型,允许与任何模型建立关系

    liked_num = models.IntegerField(default=0)


class LikeRecord(models.Model):
    objects = models.Manager()  # 加上这句才能应用objects
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # 多对一，外键指向ContentType模型
    object_id = models.PositiveIntegerField()  # 数值字段类型，存储将要关联的模型中的主键值
    content_object = GenericForeignKey('content_type', 'object_id')  # 特殊的字段类型,允许与任何模型建立关系

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_time = models.DateTimeField(auto_now_add=True)
