from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseRedirect


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        user_name = request.POST['username']
        password = request.POST['password']
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=user_name, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')

    else:
        form = AuthenticationForm()

    return render(request, 'user_template/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')  # we can refer to every page we want such: '/users/login'


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            '''
            # if write below codes, after sign up don't need to login  
            user_name = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=user_name, password=password)
            login(request, user)
            '''
            return redirect('/')

    else:
        form = UserCreationForm()

    return render(request, 'user_template/signup.html', {'form': form})


def forgotpass(request):
    pass