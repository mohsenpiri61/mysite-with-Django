from django import template
from blog_app.models import Post, Category

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


@register.inclusion_tag('blog_items/blog-post-categories.html')
def cat_of_posts():
    post_obj = Post.objects.filter(status=1)
    category_obj = Category.objects.all()
    cat_dict = {}
    for cat_name in category_obj:
        cat_dict[cat_name] = post_obj.filter(category_list=cat_name).count()
    return {'cat_dict': cat_dict}
