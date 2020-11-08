# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@CreateDate: 2020/11/3 21:41
@FileName: urls.py
@FuncSummary: blog应用子路由
@Author: WU RUN
@Software: PyCharm
@Version: 1.0
@Update:
@Copyright:
"""

from django.urls import path
from . import views

# 应用路由。子路由
urlpatterns = [
    # http://localhost:8000/blog/1
    path('', views.blog_list, name='blog_list'),  # 博客列表链接
    path('<int:blog_pk>', views.blog_detail, name="blog_detail"),  # url参数须于视图函数中参数相同
    path('type/<int:blog_type_pk>', views.blogs_with_type, name="blogs_with_type"),
    path('date/<int:year>/<int:month>', views.blogs_with_date, name='blogs_with_date'),  # 当前年月的博客
]