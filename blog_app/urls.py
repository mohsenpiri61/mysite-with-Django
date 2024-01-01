from django.urls import path
from blog_app.views import *

app_name = 'blog_show'

urlpatterns = [
    path('home', home_view, name='home'),
    path('single', single_view, name='single')
]
