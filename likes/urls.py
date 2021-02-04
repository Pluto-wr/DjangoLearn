# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@CreateDate: 2020/11/16 21:31
@FileName: urls.py
@FuncSummary: 点赞/取消点赞url
@Author: WU RUN
@Software: PyCharm
@Version: 1.0
@Update:
@Copyright: 
"""

from django.urls import path
from . import views

urlpatterns = [
    path('like_change', views.like_change, name='like_change'),  # 处理评论
]