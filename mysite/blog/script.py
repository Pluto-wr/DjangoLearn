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
        import os
        import sys
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 定位到你的django根目录
        sys.path.append(os.path.abspath(os.path.join(BASE_DIR, os.pardir)))
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")  # 你的django的settings文件
        import django
        django.setup()
        from blog.models import BlogType, Blog
        from django.contrib.auth.models import User
        # 循环生成博客列表数据
        for i in range(1, 31):
            blog = Blog()
            blog.title = '循环下面第%d篇' % i
            blog.content = '今天真是开心的一天'
            blog_type = BlogType.objects.all()[0]
            blog.blog_type = blog_type
            user = User.objects.all()[0]
            blog.author = user
            # blog.save()
            blog.save()
            print(blog)
            blog1 = Blog.objects.count()
            print(blog1)
    except Exception:
        raise


