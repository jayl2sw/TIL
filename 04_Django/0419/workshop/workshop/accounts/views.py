import re
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as auth_login, logout as auth_logout, get_user_model
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserChangeForm, CustomUserCreationFrom
# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == "POST":
        form = CustomUserCreationFrom(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationFrom()
    context = {
        'form':form
    }
    return render(request, 'accounts/signup.html', context)


def signin(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/signin.html', context)

def signout(request):
    if request.method == "POST":
        auth_logout(request)
    return redirect('articles:index')


def profile(request, username):
    person = get_object_or_404(get_user_model(), username = username)
    
    context = {
        'person': person
    }
    return render(request, 'accounts/profile.html', context)

def follow(request, username):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), username = username)        
        if person.followers.filter(pk=request.user.pk).exists():
            person.followers.remove(request.user)
        else:
            person.followers.add(request.user)

        return redirect('accounts:profile', person.username)
    return redirect('accounts:login')
