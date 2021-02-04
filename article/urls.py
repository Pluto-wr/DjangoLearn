# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@CreateDate: 2020// :
@FileName: .py
@FuncSummary: 
@Author: WU RUN
@Software: PyCharm
@Version: 1.0
@Update:
@Copyright: Copyright@厦门科拓通讯技术股份有限公司 
"""

from django.urls import path
from . import views

# 应用路由。子路由
urlpatterns = [
    path('<int:article_id>', views.article_detail, name="article_detail"),  # url参数须于视图函数中参数相同
    path('', views.article_list, name="article_list"),  # url参数须于视图函数中参数相同
]