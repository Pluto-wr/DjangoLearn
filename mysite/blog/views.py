from django.shortcuts import render, render_to_response, get_object_or_404
from .models import Blog, BlogType

# Create your views here.


# 博客列表视图
def blog_list(request):
    context = {}
    # 获取Blog, BlogType的所有字段内容, 返回字典
    context.update(blogs=Blog.objects.all(), blog_types=BlogType.objects.all())
    return render(request, 'blog/blog_list.html', context)


# 具体的博客视图
def blog_detail(request, blog_pk):
    context = {}
    context.update(blog=get_object_or_404(Blog, pk=blog_pk))
    return render_to_response('blog/blog_detail.html', context)


# 筛选博客类型
def blogs_with_type(request, blog_type_pk):
    context = {}
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    context.update(blogs=Blog.objects.filter(blog_type=blog_type), blog_type=blog_type, blog_types=BlogType.objects.all())
    return render_to_response('blog/blogs_with_type.html', context)

