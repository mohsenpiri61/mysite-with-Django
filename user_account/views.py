from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


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


def signup_view(request):
    return render(request, 'user_template/signup.html')
