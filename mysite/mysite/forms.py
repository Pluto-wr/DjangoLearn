# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@CreateDate: 2020/11/8 18:59
@FileName: forms.py
@FuncSummary: django-forms表单，input==字段, label标签为 input 元素定义标注
              验证相关操作放在form里面。
@Author: WU RUN
@Software: PyCharm
@Version: 1.0
@Update:
@Copyright: 
"""

from django import forms
from django.contrib import auth
from django.contrib.auth.models import User


# 登录表单
class LoginForm(forms.Form):
    username = forms.CharField(label='用户名',
                               widget=forms.TextInput(
                                            attrs={'class': 'form-control', 'placeholder': '请输入用户名'}))
    password = forms.CharField(label='密码',
                               widget=forms.PasswordInput(
                                            attrs={'class': 'form-control', 'placeholder': '请输入密码'}))  # 定义input的类型

    # 登录用户验证
    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = auth.authenticate(username=username, password=password)  # 用户认证, 返回user对象
        if user is None:
            raise forms.ValidationError('用户名或密码不正确')
        else:
            self.cleaned_data['user'] = user  # 写入验证通过的user对象
        return self.cleaned_data  # 方法要求


# 注册
class RegForm(forms.Form):
    username = forms.CharField(label='用户名',
                               max_length=30,
                               min_length=3,
                               widget=forms.TextInput(
                                    attrs={'class': 'form-control', 'placeholder': '请输入3-30位用户名'}))
    email = forms.EmailField(label='邮箱',
                             widget=forms.TextInput(
                                    attrs={'class': 'form-control', 'placeholder': '请输入邮箱'}))
    password = forms.CharField(label='密码',
                               min_length=6,
                               widget=forms.PasswordInput(
                                   attrs={'class': 'form-control', 'placeholder': '请输入密码'}))
    password_again = forms.CharField(label='再次输入密码',
                                     min_length=6,
                                     widget=forms.PasswordInput(
                                        attrs={'class': 'form-control', 'placeholder': '请再次输入密码'}))

    # 针对用户名进行验证
    def clean_username(self):
        username = self.cleaned_data['username']  # 通过cleaned_data获取
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('用户名已存在')
        return username

    # 针对邮箱进行验证
    def clean_email(self):
        email = self.cleaned_data['email']  # 通过cleaned_data获取
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('邮箱已存在')
        return email

    # 对密码进行验证
    def clean_password_again(self):
        password = self.cleaned_data['password']
        password_again = self.cleaned_data['password_again']
        if password != password_again:
            raise forms.ValidationError('两次输入的密码不一致')
        return password_again
