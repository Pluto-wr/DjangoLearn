from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, render_to_response, get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.core.cache import cache
from .utils import get_seven_days_read_data, get_today_hot_data, get_week_hot_data
from blog.models import Blog


def num_statistics(request):
    blog_content_type = ContentType.objects.get_for_model(Blog)
    dates, read_nums = get_seven_days_read_data(blog_content_type)
    # 获取7天热门博客的缓存数据
    week_hot = cache.get('week_hot')
    if week_hot is None:
        week_hot = get_week_hot_data()
        cache.set('week_hot', week_hot, 3600)
    context = {}
    context.update(read_nums=read_nums,
                   dates=dates,
                   today_hot=get_today_hot_data(blog_content_type),
                   week_hot=week_hot)
    return render(request, 'statistics/statistics.html', context)

