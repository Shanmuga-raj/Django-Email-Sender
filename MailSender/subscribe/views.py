from django.shortcuts import render
from MailSender import settings
from . import forms
from django.core.mail import send_mail


# Create your views here.

def subscribe(request):
    sub = forms.Subscribe()

    if request.method == "POST":
        sub = forms.Subscribe(request.POST)
        subject = 'Django EMail Test'
        message = 'Hey, This is a test message using django!!'
        recepient = str(sub['Email'].value())
        send_mail(subject, message, settings.EMAIL_HOST_USER, [recepient], fail_silently=False)
        return render(request, 'subscribe/success.html', {'recepient': recepient})

    return render(request, 'subscribe/index.html', {'form': sub})

