# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@CreateDate: 2020/11/7 00:01
@FileName: utils.py
@FuncSummary: 根据cookie读取一次博客的统计计数
@Author: WU RUN
@Software: PyCharm
@Version: 1.0
@Update:
@Copyright: 
"""
from django.contrib.contenttypes.models import ContentType
from .models import ReadNum


def read_statistics_once_read(request, obj):
    """
    读取一次博客统计基数
    :param request: 请求
    :param obj: 具体的模型的对象
    :return:
    """
    ct = ContentType.objects.get_for_model(obj)  # 获取具体的模型对象的模型类实例
    key = f'{ct.model}_{obj.pk}_read'  # key==cookie ct.model获取模型类的名称， obj.pk具体对象的主键值
    if not request.COOKIES.get(key):
        if ReadNum.objects.filter(content_type=ct, object_id=obj.pk).count():  # 筛选Blog id 不为0 true
            readnum = ReadNum.objects.get(content_type=ct, object_id=obj.pk)  # 存在记录 取出这条blog记录
        else:
            readnum = ReadNum(content_type=ct, object_id=obj.pk)  # 不存在对应记录创建记录，实例化ReadNum()类
        readnum.read_num += 1  # 进入到这篇博客就把read_num + 1
        readnum.save()  # 全局保存，相当于修改
    return key
