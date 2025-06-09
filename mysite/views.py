from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from . import forms, models


def main(request):
    """Обработчик главной страницы платформы"""
    data = {}


def login_view(request):
    """Обработчик страницы авторизации в системе"""
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("index")
    else:
        form = forms.LoginForm()
    return render(request, "auth/login.html", {"form": form})


def register(request):
    """Обработчик страницы регистрации в системе"""
    if request.method == "POST":
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("login")
    else:
        form = forms.RegisterForm()
    return render(request, "auth/register.html", {"form": form})


def logout_view(request):
    """Обработчик страницы выхода из системы"""
    logout(request)
    return redirect("login")
    
    
def courses(request):
    data = {
        "solutions": models.Solution.objects.all()
    }
    return render(request, "courses.html", data)


def load_solution(request):
    if request.method == "POST":
        form = forms.SolutionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = forms.SolutionForm()
        
    data = {
        "form": form
    }
    return render(request, "loadsolution.html", data)
    