from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.paginator import Paginator  # Django自带的分页器
from .models import Blog, BlogType
from mysite import settings

# Create your views here.


# 博客列表视图
def blog_list(request):
    blogs_all_list = Blog.objects.all()  # 获取全部的博客列表
    paginator = Paginator(blogs_all_list, settings.NUMBER_OF_BLOGS_PAGES)  # 以每页10条内容进行分类
    # 获取GET请求的内容
    page_num = request.GET.get("page", 1)  # get获取页面参数，如果字典中没有已存在的page，默认返回1
    page_of_blogs = paginator.get_page(page_num)  # 判断如果得到的页码不是int或无效默认返回第1页 返回的是Page对象
    current_page_num = page_of_blogs.number  # 根据Page对象的number属性得到具体的当前页码的value
    # 获取当前页码前后2页的页码范围
    page_range = [page for page in range(current_page_num-2, current_page_num+3) if page > 0 and page <= paginator.num_pages]

    # 分页中加上省略号标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, "...")
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append("...")
    # 判断显示第1页与最后一页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context = {}
    # 获取Blog, BlogType的所有字段内容, 返回字典,
    context.update(blogs=page_of_blogs.object_list,
                   page_of_blogs=page_of_blogs,
                   page_range=page_range,
                   blog_types=BlogType.objects.all())
    return render_to_response('blog/blog_list.html', context)


# 具体的博客内容视图
def blog_detail(request, blog_pk):
    context = {}
    context.update(blog=get_object_or_404(Blog, pk=blog_pk))
    return render_to_response('blog/blog_detail.html', context)


# 根据博客类型获取到博客
def blogs_with_type(request, blog_type_pk):
    context = {}
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    blogs_all_list = Blog.objects.filter(blog_type=blog_type)  # 获取根据类型筛选出的博客列表
    paginator = Paginator(blogs_all_list, settings.NUMBER_OF_BLOGS_PAGES)  # 以每页10条内容进行分类
    # 获取GET请求的内容
    page_num = request.GET.get('page', 1)  # get获取页面参数，如果字典中没有已存在的page，默认返回1
    page_of_blogs = paginator.get_page(page_num)  # 判断如果得到的页码不是int或无效默认返回第1页 返回的是Page对象
    current_page_num = page_of_blogs.number  # 根据Page对象的number属性得到具体的当前页码的value
    # 获取当前页码前后2页的页码范围
    page_range = [page for page in range(current_page_num - 2, current_page_num + 3) if page > 0 and page <= paginator.num_pages]

    # 分页中加上省略号标记
    if page_range[0] - 1 >= 2:
        page_range.insert(0, "...")
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')
    # 判断显示第1页与最后一页
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    # context = {}
    # 获取Blog, BlogType的所有字段内容, 返回字典,
    context.update(blog_type=blog_type,
                   blogs=page_of_blogs.object_list,
                   page_of_blogs=page_of_blogs,
                   page_range=page_range,
                   blog_types=BlogType.objects.all())

    return render_to_response('blog/blogs_with_type.html', context)


