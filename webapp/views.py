from django.http import HttpResponse, JsonResponse
def home_view(request):
    return HttpResponse('<h1> You are in Home page </h1>')

def about_text(request):
    return HttpResponse('<h1> About </h1>')

def contact_list(request):
    return JsonResponse({'name': 'mohsen', 'age': 41})