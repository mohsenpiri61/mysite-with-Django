from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def home_text(request):
    return HttpResponse('<h1> You are in Home page </h1>')

def about_text(request):
    return HttpResponse('<h1> About </h1>')

def contact_text(request):
    return JsonResponse({'name': 'mohsen', 'age': 41})

def index_view(request): # refer to templates folder
    return render(request, 'index.html')

def about_view(request): # refer to templates folder
    return render(request, 'about.html')

def contact_view(request): # refer to templates folder
    return render(request, 'contact.html')

def elements_view(request): # refer to templates folder
    return render(request, 'elements.html')

