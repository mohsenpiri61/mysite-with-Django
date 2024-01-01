from django.shortcuts import render

def home_view(request): # refer to blog_items folder in template folder
    return render(request, 'blog_items/blog-home.html')

def single_view(request): # refer to blog_items folder in template folder
    return render(request, 'blog_items/blog-single.html')

