from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import auth
from django.contrib import messages
from .forms import SignUpForm


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            user_input = request.POST['username']
            try:
                user_name = User.objects.get(email=user_input).username
            except User.DoesNotExist:
                user_name = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=user_name, password=password)
            if user is not None:
                auth.login(request, user)
                messages.add_message(request, messages.SUCCESS, 'Login was successful')
                return redirect('/')
            else:
                messages.add_message(request, messages.ERROR, 'The user was not found')
        return render(request, "user_template/login.html")
    else:
        return redirect('/')


def logout_view(request):
    logout(request)
    return redirect('/')  # we can refer to every page we want such: '/users/login'


def signup_view(request):

    if not request.user.is_authenticated:
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        form = SignUpForm()
        context = {'form': form}
        return render(request, 'user_template/signup.html', context)
    else:
        return redirect('/')

