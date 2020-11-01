from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Article
# Create your views here.
"""
index函数必须设置参数request，该参数代表当前用户的请求对象，该对象包含用户名、请求内容和请求方式等信息，
视图函数执行完成后必须使用return将处理结果返回，否则程序会抛出异常信息
"""


def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)  # 操作模型对象，根据传入id的记录获取, 如不存在返回404，pk是主键的缩写
    context = {}
    context.update(article_obj=article)
    # return render(request, "article_detail.html", )
    return render_to_response("article_detail.html", context)  # 渲染模板，显示页面


# 文章列表
def article_list(request):
    # articles = Article.objects.all()  # 返回全部对象
    articles = Article.objects.filter(is_deleted=False)  # 筛选出没有删除的对象
    context = {}
    context.update(articles=articles)
    return render_to_response("article_list.html", context)
