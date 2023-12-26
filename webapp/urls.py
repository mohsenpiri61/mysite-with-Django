from django.urls import path
from webapp.views import *

urlpatterns = [
    path('home', home_view),
    path('about', about_text),
    path('contact', contact_list),
    path('index', index_show)
]
