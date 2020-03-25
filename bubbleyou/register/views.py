from django.shortcuts import render,redirect
from .forms import RegisterForm


def register(response):
    if response.method=="POST":
        form= RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("/header")
    else:
        form = RegisterForm()
    return render(response,'signup.html', {"form": form})
