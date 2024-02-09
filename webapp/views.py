from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from webapp.models import Contact
from webapp.forms import NameForm, ContactForm, NewsletterForm
from django.contrib import messages


def home_text(request):
    return HttpResponse('<h1> You are in Home page </h1>')


def about_text(request):
    return HttpResponse('<h1> About </h1>')


def contact_text(request):
    return JsonResponse({'name': 'mohsen', 'age': 41})


def index_view(request):
    return render(request, 'index.html')


def about_view(request):
    return render(request, 'about.html')


def contact_view(request):
    if request.method == 'POST':
        form_data = ContactForm(request.POST)
        if form_data.is_valid():
            contact = form_data.save(commit=False)
            contact.name = 'anonymous'
            contact.save()
            messages.add_message(request, messages.SUCCESS, 'save information successfully')
        else:
            messages.add_message(request, messages.ERROR, 'save information not successfully')
    form_data = ContactForm()
    return render(request, 'contact.html', {'form_data': form_data})  # we don't need to send {'form_data': form_data} into contact.html




def newsletter_view(request):
    if request.method == 'POST':
        form_data = NewsletterForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponseRedirect('/')  # '/' means go to the Home ,'/contact' means go to the contact

    else:
        return HttpResponseRedirect('/')


def elements_view(request):  # refer to templates folder
    return render(request, 'elements.html')


def form_view(request):
    if request.method == 'POST':
        name = request.POST.get('your_name')
        email = request.POST.get('email_form')
        subject = request.POST.get('subject_form')
        message = request.POST.get('message_form')
        contact_form = Contact()
        contact_form.name = name
        contact_form.email = email
        contact_form.subject = subject
        contact_form.message = message
        contact_form.save()
        print(name, email, message, subject)

    return render(request, 'form-test.html')


def form2_view(request):
    if request.method == 'POST':
        form_data = NameForm(request.POST)
        if form_data.is_valid():
            form_name = form_data.cleaned_data['Name']
            form_lastname = form_data.cleaned_data['Lastname']
            print('First name is:', form_name)
            return HttpResponse('done')
    else:
        form_data = NameForm()

    return render(request, 'form2-test.html', {'form_data': form_data})


def form3_view(request):
    if request.method == 'POST':
        form_data = ContactForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('done')
    else:
        form_data = ContactForm()

    return render(request, 'form3-test.html', {'form_data': form_data})

'''
def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        form_data = Contact()
        form_data.name = 'anonymous'
        form_data.email = email
        form_data.message = message
        form_data.subject = subject
        form_data.save()
        try:
            messages.add_message(request, messages.SUCCESS, 'Your ticket submitted successfully.')
        except:
            messages.add_message(request, messages.ERROR, "Your ticket didn't submitted .")
    else:
        form_data = Contact()

    return render(request, 'contact.html')
'''