from django.urls import path
from webapp.views import *

urlpatterns = [
    path('home_web', home_text),
    path('about_web', about_text),
    path('contact_web', contact_text),
    path('', index_view, name='index'),  # if was used path = ('webapp/', include('webapp.urls')) , here must use 'index'
    path('about', about_view, name='about'),
    path('contact', contact_view, name='contact'),
    path('elements', elements_view, name='elements'),
    path('contact', contact_view, name='contact')

]