# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@CreateDate: 2020/11/15 14:45
@FileName: comment_tags.py
@FuncSummary: 评论相关模板标签,解耦blog views function
@Author: WU RUN
@Software: PyCharm
@Version: 1.0
@Update:
@Copyright: 
"""

from django import template
from django.contrib.contenttypes.models import ContentType
from ..models import Comment
from ..forms import CommentForm


register = template.Library()


@register.simple_tag
def get_comment_form(obj):
    content_type = ContentType.objects.get_for_model(obj)
    # 初始化CommentForm传入对应的参数渲染到模板给前端
    form = CommentForm(initial={'content_type': content_type.model,  # 这是是将模型Blog对象转成字符串
                                'object_id': obj,
                                'reply_comment_id': 0})
    return form
