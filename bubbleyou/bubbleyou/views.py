from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')
def header(request):
    return render(request, 'header.html')
def contacts(request):
    return render(request, 'contacts.html')
def signup(request):
    return render(request, 'signup.html')
def posts(request):
    return render(request, 'posts.html')