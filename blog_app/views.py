from django.shortcuts import render, get_object_or_404
from blog_app.models import Post, Comment
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home_view(request, **kwargs):
    # To display posts whose publication date is before the current day and status=1#
    filter_post = Post.objects.filter(published_date__lt=timezone.now(), status=1)

    if kwargs.get('cat_name') != None:
        filter_post = filter_post.filter(category_list__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        filter_post = filter_post.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        filter_post = filter_post.filter(tags__name__in=[kwargs['tag_name']])

    page_init = Paginator(filter_post, 2)  # creating a paginator object, Show  ... posts per page
    page_number = request.GET.get('page')

    try:
        # getting the desired page number from url
        filter_post = page_init.get_page(page_number)
        print(filter_post.object_list)
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        filter_post = page_init.page(1)
    except EmptyPage:
        # if page is empty then return last page
        filter_post = page_init.page(page_init.num_pages)
    context = {'filter_post': filter_post}
    return render(request, 'blog_items/blog-home.html', context)


def single_view(request, pid):
    post_obj = get_object_or_404(Post, id=pid, status=1, published_date__lt=timezone.now())
    post_obj.counted_views = post_obj.counted_views + 1
    post_obj.save()

    comments = Comment.objects.filter(intended_post=post_obj.id, approved=True)

    filter_post = Post.objects.filter(published_date__lt=timezone.now(), status=1)
    post_ids = [post.id for post in filter_post]
    pid_index = post_ids.index(pid)
    if pid_index == 0:
        next_id = post_ids[pid_index+1]
        next_post = Post.objects.get(id=next_id)
        prev_post = None
    elif pid_index == post_ids.index(post_ids[-1]):
        prev_id = post_ids[pid_index-1]
        prev_post = Post.objects.get(id=prev_id)
        next_post = None
    else:
        next_id = post_ids[pid_index+1]
        next_post = Post.objects.get(id=next_id)
        prev_id = post_ids[pid_index - 1]
        prev_post = Post.objects.get(id=prev_id)
    context = {'post_obj': post_obj, 'next_post': next_post, 'prev_post': prev_post, 'comments': comments}
    return render(request, 'blog_items/blog-single.html', context)
'''
we can use this code and filter based on other fields: published_date, created_date, ...
def single2_view(requests, pid):
    post = get_object_or_404(Post, pk=pid, status=1, published_date__lte=timezone.now())
    next_post = Post.objects.filter(status=1, published_date__lte=timezone.now(), id__gt=post.id).first()
    prev_post = Post.objects.filter(status=1, published_date__lte=timezone.now(), id__lt=post.id).last()
    context = {'post': post, 'prev_post': prev_post, 'next_post': next_post}
    return render(requests, 'blog_items/blog-single.html', context)
'''
def test_view(request):
    return render(request, 'blog_items/simple_tag_test.html')


def search_view(request):
    #print(request.__dict__.keys())
    filter_post = Post.objects.filter(published_date__lt=timezone.now(), status=1)
    if request.method == 'GET':
        #print(request.GET.get('s'))
        if req := request.GET.get('s'):
            filter_post = filter_post.filter(content__contains=req)  # warlus

    context = {'filter_post': filter_post}
    return render(request, 'blog_items/blog-home.html', context)


