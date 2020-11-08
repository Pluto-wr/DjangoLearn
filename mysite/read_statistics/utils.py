# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@CreateDate: 2020/11/7 00:01
@FileName: utils.py
@FuncSummary: 统计计数
@Author: WU RUN
@Software: PyCharm
@Version: 1.0
@Update:
@Copyright: 
"""
import datetime
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.db.models import Sum
from .models import ReadNum, ReadDetail
from blog.models import Blog


def read_statistics_once_read(request, obj):
    """
    第一部分：blog总阅读读数+1， 第二部分：对当天打开的blog阅读数+1
    :param request: 请求
    :param obj: 具体的模型对象
    :return: 返回是否阅读的cookie
    """
    ct = ContentType.objects.get_for_model(obj)  # 获取具体的模型对象的模型类实例
    key = f'{ct.model}_{obj.pk}_read'  # key==cookie ct.model获取模型类的名称， obj.pk具体对象的主键值
    if not request.COOKIES.get(key):
        # 根据模型对象实例，主键值查询记录，如果不存在就创建一条记录，返回tuple
        readnum, created = ReadNum.objects.get_or_create(content_type=ct, object_id=obj.pk)
        readnum.read_num += 1  # 进入到这篇博客就把read_num + 1
        readnum.save()  # 全局保存

        date = timezone.now().date()
        readDetail, created = ReadDetail.objects.get_or_create(content_type=ct, object_id=obj.pk, date=date)
        readDetail.read_num += 1
        readDetail.save()
    return key


# content_type # 类型
def get_seven_days_read_data(content_type):
    today = timezone.now().date()
    dates = []
    read_nums = []
    for i in range(6, -1, -1):
        date = today - datetime.timedelta(days=i)
        dates.append(date.strftime('%m/%d'))
        read_datails = ReadDetail.objects.filter(content_type=content_type, date=date)
        # 对ReadDetail的read_num字段进行聚合求和，获取到当天所有的阅读明细 aggregate返回dict
        result = read_datails.aggregate(read_num_sum=Sum('read_num'))
        read_nums.append(result['read_num_sum'] or 0)
    return dates, read_nums


# 获取今天的热门博客
def get_today_hot_data(content_type):
    today = timezone.now().date()
    #   对read_num倒叙排序
    read_details = ReadDetail.objects.filter(content_type=content_type, date=today).order_by('-read_num')
    return read_details[:6]  # ---> QuerySet


# 获取7天的热门博客
def get_week_hot_data():
    today = timezone.now().date()
    date = today - datetime.timedelta(days=7)
    # 分组求和，values--> QuerySet用作迭代器时返回的dict, dict中的每一个都代表一个对象，其键对应于模型对象的属性名称。
    # values分组--> 对传入的对象,主键值进行分组后对read_num求和
    read_details = Blog.objects \
                       .filter(read_details__date__lt=today, read_details__date__gte=date) \
                       .values('id', 'title') \
                       .annotate(read_num_sum=Sum('read_details__read_num')) \
                       .order_by('-read_num_sum')
    return read_details[:6]
