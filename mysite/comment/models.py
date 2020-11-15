from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey # 外键


# Create your models here.
# 主引用从,即一对多, 外键字段是放在多的一端的
# User主，Comment从，comment访问user很好访问，user访问comment不好访问，所以设置一个related_name属性
class Comment(models.Model):
    # 对应任何类型的字段
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)  # 多对一，外键指向ContentType模型
    object_id = models.PositiveIntegerField()  # 数值字段类型，存储将要关联的模型中的主键值
    content_object = GenericForeignKey('content_type', 'object_id')  # 特殊的字段类型,允许与任何模型建立关系

    text = models.TextField()
    comment_time = models.DateTimeField(auto_now_add=True)
    # 什么用户写的评论,related_name反向关联。主可以user.comments.all()访问从
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)

    root = models.ForeignKey('self', related_name='root_comment', null=True, on_delete=models.CASCADE)  # 顶级回复
    parent = models.ForeignKey('self', related_name='parent_comment', null=True, on_delete=models.CASCADE)  # 外键指向自身
    reply_to = models.ForeignKey(User, related_name='replies', null=True, on_delete=models.CASCADE)  # 回复很么用户的评论

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['comment_time']

