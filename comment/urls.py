# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@CreateDate: 2020/11/8 13:47
@FileName: .py
@FuncSummary: 评论相关子路由
@Author: WU RUN
@Software: PyCharm
@Version: 1.0
@Update:
@Copyright: 
"""

from django.urls import path
from . import views

urlpatterns = [
    path('update_comment', views.update_comment, name='update_comment'),  # 处理评论
]