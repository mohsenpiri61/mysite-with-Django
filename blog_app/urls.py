from django.urls import path
from blog_app.views import *


app_name = 'blog_show'

urlpatterns = [
    path('', home_view, name='home_blog'),
    path('<int:pid>', single_view, name='single_blog'),
    path('category/<str:cat_name>', home_view, name='category_blog'),
    path('tag/<str:tag_name>', home_view, name='tag_blog'),
    path('author/<str:author_username>', home_view, name='author_pubs'),
    path('search/', search_view, name='search_index'),
    path('test', test_view)


]