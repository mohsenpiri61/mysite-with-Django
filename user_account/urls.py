from django.urls import path
from user_account.views import *


app_name = 'user_auth'

urlpatterns = [
    path('login', login_view, name='login_page'),
    path('logout', logout_view, name='logout_page'),
    path('signup', signup_view, name='signup_page'),
    path('forgot', forgotpass, name='forgot_page')
   # path('password_reset', views.password_reset, name='password_reset'),

]