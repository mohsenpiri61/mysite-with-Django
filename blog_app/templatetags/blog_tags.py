from django import template
from blog_app.models import Post

register = template.Library()


@register.simple_tag()
def cal_post():
    posts = Post.objects.filter(status=1).count()
    return posts


@register.simple_tag(name='posts')
def show_post():
    posts_obj = Post.objects.filter(status=1)
    return posts_obj


@register.filter
def snippet(value, count):
    return value[:count]


@register.inclusion_tag('popular-post-view.html')
def show_popularposts():
    post_obj = Post.objects.filter(status=1).order_by('-published_date')[:3]
    return {'post_obj': post_obj}


@register.inclusion_tag('blog_items/blog-latest-post.html')
def latestposts(arg=3):
    post_obj = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'post_obj': post_obj}
