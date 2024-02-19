from django.urls import path
from user_account.views import *
from django.contrib.auth import views

app_name = 'user_auth'

urlpatterns = [
    path('login', login_view, name='login_page'),
    path('logout', logout_view, name='logout_page'),
    path('signup', signup_view, name='signup_page'),
    path('password_reset', views.PasswordResetView.as_view(template_name="user_template/password_reset_form.html",
         email_template_name="user_template/password_reset_email.html",
         success_url='password_reset/done'), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(
         template_name="user_template/password_reset_done.html"), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(
         template_name="user_template/password_reset_confirm.html",
         success_url="password_reset/complete"), name='password_reset_confirm'),
    path('password_reset/complete/', views.PasswordResetCompleteView.as_view(
         template_name="user_template/password_reset_complete.html"), name='password_reset_complete')

]
