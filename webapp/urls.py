from django.urls import path
from webapp.views import *
from django.contrib.sitemaps.views import sitemap
from webapp.sitemaps import StaticViewSitemap
from blog_app.sitemaps import BlogSitemap


sitemaps = {"static": StaticViewSitemap, 'blog_app': BlogSitemap,}

urlpatterns = [
    path('home_web', home_text),
    path('about_web', about_text),
    path('contact_web', contact_text),
    path('', index_view, name='index'),  # if was used path = ('webapp/', include('webapp.urls')) , here must use 'index'
    path('about', about_view, name='about'),
    path('contact', contact_view, name='contact'),
    path('elements', elements_view, name='elements'),
    path('contact', contact_view, name='contact'),
    path('forms', form_view, name='form-init'),
    path('forms2', form2_view, name='form2-init'),
    path('forms3', form3_view, name='form3-init'),
    path('newsletter', newsletter_view, name='newsletter'),
    path(
        "sitemap.xml", sitemap, {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    )

]