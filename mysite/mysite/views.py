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

from django.shortcuts import render, render_to_response, get_object_or_404


def home(request):
    context = {}
    return render_to_response('home.html', context)