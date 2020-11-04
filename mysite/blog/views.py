from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.paginator import Paginator  # Django自带的分页器
from .models import Blog, BlogType
from mysite import settings

# Create your views here.


def get_blogs_list_common_data(request, blogs_all_list):
    paginator = Paginator(blogs_all_list, settings.NUMBER_OF_BLOGS_PAGES)  # 以每页10条内容进行分类
    # 获取GET请求的内容
    page_num = request.GET.get("page", 1)  # get获取页面参数，如果字典中没有已存在的page，默认返回1
    page_of_blogs = paginator.get_page(page_num)  # 判断如果得到的页码不是int或无效默认返回第1页 返回的是Page对象
    current_page_num = page_of_blogs.number  # 根据Page对象的number属性得到具体的当前页码的value
    # 获取当前页码前后2页的页码范围
    page_range = [page for page in range(current_page_num - 2, current_page_num + 3) if page > 0 and page <= paginator.num_pages]

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
                   blog_types=BlogType.objects.all(),
                   # (字段，类型，排序) 此方法返回一个QuerySet，提供可用的日期了些，类型包括year,month,day,这里返回年-月的所有博客list, 降序
                   blog_dates=Blog.objects.dates('created_time', 'month', order='DESC'),
                   )
    return context


# 博客列表视图
def blog_list(request):
    blogs_all_list = Blog.objects.all()  # 获取全部的博客列表
    context = get_blogs_list_common_data(request, blogs_all_list)
    return render_to_response('blog/blog_list.html', context)


# 具体的博客内容视图
def blog_detail(request, blog_pk):
    context = {}
    blog = get_object_or_404(Blog, pk=blog_pk)  # ==Blog.objects.get(pk=blog_pk)，根据主键id获取到这篇博文的具体内容
    context.update(blog=blog,
                   # 通过filter的__gt方法筛选出大于当前博客创建时间的创建的博客取最后一个为上一篇
                   previous_blog=Blog.objects.filter(created_time__gt=blog.created_time).last(),
                   # 通过filter的__lt方法筛选出小于当前博客创建时间的创建的博客取最前一个为下一篇
                   next_blog=Blog.objects.filter(created_time__lt=blog.created_time).first(),
                   )
    return render_to_response('blog/blog_detail.html', context)


# 根据博客类型获取到博客
def blogs_with_type(request, blog_type_pk):

    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    blogs_all_list = Blog.objects.filter(blog_type=blog_type)  # 获取根据类型筛选出的博客列表
    context = get_blogs_list_common_data(request, blogs_all_list)
    # context = {}
    # 获取Blog, BlogType的所有字段内容, 返回字典,
    context.update(blog_type=blog_type)
    return render_to_response('blog/blogs_with_type.html', context)


# 根据年月获取的博客
def blogs_with_date(request, year, month):
    blogs_all_list = Blog.objects.filter(created_time__year=year, created_time__month=month)  # 获取根据类型筛选出的博客列表
    context = get_blogs_list_common_data(request, blogs_all_list)
    # 获取Blog, BlogType的所有字段内容, 返回字典,
    context.update(blogs_with_date=f'{year}年{month}月')
    return render_to_response('blog/blogs_with_date.html', context)

