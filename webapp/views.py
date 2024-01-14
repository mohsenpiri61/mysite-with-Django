from django.http import HttpResponse, JsonResponse
from django.shortcuts import render



def index_view(request): # refer to templates folder
    return render(request, 'index.html')

def about_view(request): # refer to templates folder
    return render(request, 'about.html')

def contact_view(request): # refer to templates folder
    return render(request, 'contact.html')


