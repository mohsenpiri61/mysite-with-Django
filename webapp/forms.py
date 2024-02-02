from django import forms
from webapp.models import Contact, Newsletter
#from captcha.fields import CaptchaField


class NameForm(forms.Form):
    Name = forms.CharField(max_length=100)
    Lastname = forms.CharField(max_length=100)


class ContactForm(forms.ModelForm):
    #captcha = CaptchaField()
    class Meta:
        model = Contact
        fields = '__all__'


class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'
