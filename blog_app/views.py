from django.shortcuts import render, get_object_or_404
from blog_app.models import Post
from django.utils import timezone

def home_view(request):  # refer to blog_items folder in template folder
    # To display posts whose publication date is before the current day and status=1#
    '''  filter_post = Post.objects.filter(published_date__lt=timezone.now(), status=1) '''
    filter_post = Post.objects.filter(status=1)
    context = {'post_filtered': filter_post}
    return render(request, 'blog_items/blog-home.html', context)


def single_view(request, pid):  # refer to blog_items folder in template folder
    post_id = get_object_or_404(Post, id=pid)
    post_id.counted_views = post_id.counted_views + 1
    post_id.save()
    context = {'post_obj': post_id}
    return render(request, 'blog_items/blog-single.html', context)


def fetch_view(request):  # refer to templates folder
    all_post = Post.objects.all()
    filter_post = Post.objects.filter(status=0)
    context = {'post_list': all_post, 'post_filtered': filter_post}
    return render(request, 'fetch.html', context)


def urlpara_view(request, pid):  # refer to templates folder
    #post_id = Post.objects.get(id=pid)
    post_id = get_object_or_404(Post, id=pid)
    context = {'post_num': post_id}
    return render(request, 'urlpara.html', context)




