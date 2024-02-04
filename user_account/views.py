from django.shortcuts import render


def login_view(request):
    if request.user.is_authenticated:
        msg = f'user is loggined as {request.user.username}'
    else:
        msg = 'user is not loggined'
    return render(request, 'user_template/login.html', {'msg': msg})


def signup_view(request):
    return render(request, 'user_template/signup.html')