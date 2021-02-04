# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@CreateDate: 2020/11/7 16:51
@FileName: urls.py
@FuncSummary: read_statistics 子路由模块
@Author: WU RUN
@Software: PyCharm
@Version: 1.0
@Update:
@Copyright: 
"""

from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/blog/1
    path('', views.num_statistics, name='num_statistics'),  # 阅读数量统计
]