from django.shortcuts import redirect, render
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from .models import Comment


# 处理前端提交的评论请求
def update_comment(request):
    referer = request.META.get('HTTP_REFERER', reverse('home'))

    if not request.user.is_authenticated:
        return render(request, 'error.html', {'message': '未登录用户', 'redirect_to': referer})
    text = request.POST.get('text', '')
    if text == '':
        return render(request, 'error.html', {'message': '评论不能为空', 'redirect_to': referer})

    try:
        content_type = request.POST.get('content_type', '')  # string
        object_id = int(request.POST.get('object_id', ''))
        model_class = ContentType.objects.get(model=content_type).model_class()
        model_obj = model_class.objects.get(pk=object_id)  # --> Blog  Blog.pk
    except Exception:
        return render(request, 'error.html', {'message': '评论对象不存在', 'redirect_to': referer})

    comment = Comment()
    comment.user = request.user
    comment.text = text
    comment.content_object = model_obj
    comment.save()
    return redirect(referer)  # 重定向跳转到当前页面，否则就跳转到首页
