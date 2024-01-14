from django.urls import path
from blog_app.views import *


app_name = 'blog_show'

urlpatterns = [
    path('home', home_view, name='home_blog'),
    path('<int:pid>', single_view, name='single_blog'),
    path('fetch', fetch_view)
    #path('post/<int:pid>', urlpara_view )

]