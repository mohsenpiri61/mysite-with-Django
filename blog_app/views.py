from django.shortcuts import render, get_object_or_404
from blog_app.models import Post
from django.utils import timezone


def home_view(request, cat_name=None):
    # To display posts whose publication date is before the current day and status=1#
    filter_post = Post.objects.filter(published_date__lt=timezone.now(), status=1)
    #filter_post = Post.objects.filter(status=1)  # posts that only have status=1
    if cat_name:
        filter_post = filter_post.filter(category_list__name=cat_name)
    context = {'filter_post': filter_post}
    return render(request, 'blog_items/blog-home.html', context)


def single_view(request, pid):  # refer to blog_items folder in template folder
    post_obj = get_object_or_404(Post, id=pid, status=1, published_date__lt=timezone.now())
    post_obj.counted_views = post_obj.counted_views + 1
    post_obj.save()
    filter_post = Post.objects.filter(published_date__lt=timezone.now(), status=1)
    post_ids = [post.id for post in filter_post]
    pid_index = post_ids.index(pid)
    if pid_index == 0:
        next_id = post_ids[pid_index+1]
        next_obj = Post.objects.get(id=next_id)
        prev_obj = Post.objects.none()
    elif pid_index == post_ids.index(len(post_ids)-1):
        prev_id = post_ids[pid_index-1]
        prev_obj = Post.objects.get(id=prev_id)
        next_obj = Post.objects.none()
    else:
        next_id = post_ids[pid_index+1]
        next_obj = Post.objects.get(id=next_id)
        prev_id = post_ids[pid_index - 1]
        prev_obj = Post.objects.get(id=prev_id)
    context = {'post_obj': post_obj, 'next_obj': next_obj, 'prev_obj': prev_obj}
    return render(request, 'blog_items/blog-single.html', context)


def test_view(request):
    return render(request, 'test.html')



