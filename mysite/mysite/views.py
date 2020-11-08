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

from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.contrib import auth
from django.urls import reverse   # 反向解析别名
from django.contrib.auth.models import User
from .forms import LoginForm, RegForm


def home(request):
    context = {}
    return render(request, 'home.html', context)


# 验证用户登录
def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)  # 提交数据给LoginForm初始化
        if login_form.is_valid():  # 验证数据是否通过，通过即获取U P
            user = login_form.cleaned_data['user']
            auth.login(request, user)  # 登录
            return redirect(request.GET.get('from', reverse('home')))  # 重定向到来的页面。否则跳转到首页
    else:
        login_form = LoginForm()
    content = {}
    content.update(login_form=login_form)
    return render(request, 'login.html', content)


# 用户注册视图方法
def register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST)  # 提交数据给RegForm初始化
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            email = reg_form.cleaned_data['email']
            password = reg_form.cleaned_data['password']
            user = User.objects.create_user(username, email, password)  # 创建
            user.save()
            # 登录用户
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return redirect(request.GET.get('from', reverse('home')))  # 重定向到来的页面。否则跳转到首页
    else:
        reg_form = RegForm()
    content = {}
    content.update(reg_form=reg_form)
    return render(request, 'register.html', content)