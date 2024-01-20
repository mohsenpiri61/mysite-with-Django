from django.urls import path
from blog_app.views import *


app_name = 'blog_show'

urlpatterns = [
    path('home', home_view, name='home_blog'),
    path('<int:pid>', single_view, name='single_blog'),
    path('category/<str:cat_name>', home_view, name='category_blog'),
    path('author/<str:author_username>', home_view, name='author_pubs'),
    path('test', test_view)
    #path('post/<int:pid>', urlpara_view )

]