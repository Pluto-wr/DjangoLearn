# !/usr/bin/python3
# -*- coding: utf-8 -*-
"""
@CreateDate: 2020// :
@FileName: .py
@FuncSummary: 循环生成博客
@Author: WU RUN
@Software: PyCharm
@Version: 1.0
@Update:
@Copyright: Copyright@厦门科拓通讯技术股份有限公司 
"""


if __name__ == '__main__':
    try:
        import os, sys, random, string, datetime
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 定位到你的django根目录
        sys.path.append(os.path.abspath(os.path.join(BASE_DIR, os.pardir)))
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")  # 你的django的settings文件
        import django
        django.setup()
        from blog.models import BlogType, Blog
        from django.contrib.auth.models import User
        # 循环生成博客列表数据
        for i in range(101, 103):
            blog = Blog()
            blog.title = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + f'第{i}篇'
            blog.content = ''.join(random.sample(string.ascii_letters + string.punctuation + string.digits, 70))
            blog_type = BlogType.objects.all()[0]
            blog.blog_type = blog_type
            user = User.objects.all()[0]
            blog.author = user
            blog.save()
            print(blog.title, f'{i}:{blog.content}\n')
        blog1 = Blog.objects.count()
        print(blog1)
    except Exception:
        raise


