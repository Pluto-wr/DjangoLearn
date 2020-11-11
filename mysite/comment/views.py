from django.shortcuts import redirect, render
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from django.urls import reverse
from .models import Comment
from .forms import CommentForm


# 处理前端提交的评论请求
def update_comment(request):
    referer = request.META.get('HTTP_REFERER', reverse('home'))
    # 根据request的POST请求的参数对CommentForm进行实例化得到具体的对象
    comment_form = CommentForm(request.POST, user=request.user)
    data = {}

    if comment_form.is_valid():
        # 检查通过，保存写入到数据库
        comment = Comment()
        comment.user = comment_form.cleaned_data['user']
        comment.text = comment_form.cleaned_data['text']  # form提交时获取
        comment.content_object = comment_form.cleaned_data['content_object']  # 根据主键获取的对象，form验证通过写入到cleaned_data

        parent = comment_form.cleaned_data['parent']
        if not parent is None:
            comment.root = parent.root if not parent.root is None else parent
            comment.parent = parent
            comment.reply_to = parent.user
        comment.save()
        # 返回数据
        data.update(status='SUCCESS',
                    username=comment.user.username,
                    comment_time=comment.comment_time.strftime('%Y-%m-%d %H:%M:%S'),
                    text=comment.text)
        if not parent is None:
            data['reply_to'] = comment.reply_to.username
        else:
            data['reply_to'] = ''
        data['pk'] = comment.pk
        data['root_pk'] = comment.root.pk if not comment.root is None else ''
    else:
        data.update(status='ERROR',
                    message=list(comment_form.errors.values())[0][0])
    return JsonResponse(data)
