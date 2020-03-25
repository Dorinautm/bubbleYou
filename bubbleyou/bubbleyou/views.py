from django.shortcuts import render
from .forms import ContactForm
# Create your views here.
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError



def home(request):
    return render(request, 'header.html')
def header(request):
    return render(request, 'header.html')
def contacts(request):
    form=ContactForm()
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            subject=f'Message from {form.cleaned_data["name"]}'
            message=form.cleaned_data["message"]
            sender=form.cleaned_data["email"]
            recipients=['balaurdorina@gmail.com']
            try:
                send_mail(subject, message,sender,recipients,fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalidule')
            return HttpResponse('woohoo you did it...')

    return render(request, 'contacts.html',{'form':form})

def posts(request):
    return render(request, 'posts.html')
def login(request):
    return render(request, 'login.html')


