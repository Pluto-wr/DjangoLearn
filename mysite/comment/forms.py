# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@CreateDate: 2020/11/9 20:59
@FileName: forms.py
@FuncSummary: 评论部分form表单
@Author: WU RUN
@Software: PyCharm
@Version: 1.0
@Update:
@Copyright: 
"""
from django import forms
from django.contrib.contenttypes.models import ContentType
from django.db.models import ObjectDoesNotExist
from ckeditor.widgets import CKEditorWidget


class CommentForm(forms.Form):
    content_type = forms.CharField(widget=forms.HiddenInput)  # hidden 隐藏输入框
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    text = forms.CharField(widget=CKEditorWidget(config_name='comment_ckeditor'),
                           error_messages={'required': '评论内容不能为空'})  # text渲染成文本框，可以输入多行

    # 子类改写父类init方法，使父类初始属性增加user，super调用父类的init，返回父类的对象的任何方法
    # https://www.cnblogs.com/nerrissa/articles/5607291.html
    def __init__(self, *args, **kwargs):
        if 'user' in kwargs:
            self.user = kwargs.pop('user')
        super(CommentForm, self).__init__(*args, **kwargs)

    def clean(self):
        """
        评论对象验证
        :return:
        """
        # 判断用户是否登录
        if self.user.is_authenticated:
            self.cleaned_data['user'] = self.user  # 如果登录，写入到cleaned_data
        else:
            raise forms.ValidationError('用户尚未登录')
        # 评论对象验证
        content_type = self.cleaned_data['content_type']
        object_id = self.cleaned_data['object_id']
        try:
            # 前端评论时传入的参数。具体为评论对象与主键
            model_class = ContentType.objects.get(model=content_type).model_class()
            model_obj = model_class.objects.get(pk=object_id)  # --> Blog  Blog.pk
            self.cleaned_data['content_object'] = model_obj
        except ObjectDoesNotExist:
            raise forms.ValidationError('评论对象不存在')
        return self.cleaned_data


