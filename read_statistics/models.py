from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey  #
from django.contrib.contenttypes.models import ContentType  # 引用 ContentType模型
from django.db.models.fields import exceptions
from django.utils import timezone
# Create your models here.


class ReadNum(models.Model):
    read_num = models.IntegerField(default=0)  # 阅读计数字段，默认0
    # blog = models.OneToOneField(Blog, on_delete=models.DO_NOTHING)  # 一对一
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)  # 多对一，外键指向ContentType模型
    object_id = models.PositiveIntegerField()  # 数值字段类型，存储将要关联的模型中的主键值
    content_object = GenericForeignKey('content_type', 'object_id')  # 特殊的字段类型,允许与任何模型建立关系


# 计数方法的扩展类，所有需要计数的模型类直接继承
class ReadNumExpandMethod():
    def get_read_num(self):
        try:
            ct = ContentType.objects.get_for_model(self)  # 获取模型类或模型实例，然后返回ContentType代表该模型的实例
            readnum = ReadNum.objects.get(content_type=ct, object_id=self.pk)  # 根据模型类实例与主键id获取到记录
            return readnum.read_num
        except exceptions.ObjectDoesNotExist:  # 如果不存在read_num, 返回0
            return 0
        # return self.readnum.read_num  # 通过外键关联的方式，取到模型ReadNum的属性（字段）read_num


# readdetial是日期间隔对象。所以不继承ReadNum
class ReadDetail(models.Model):
    date = models.DateField(default=timezone.now)
    read_num = models.IntegerField(default=0)  # 阅读计数字段，默认0
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)  # 多对一，外键指向ContentType模型
    object_id = models.PositiveIntegerField()  # 数值字段类型，存储将要关联的模型中的主键值
    content_object = GenericForeignKey('content_type', 'object_id')