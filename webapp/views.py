from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm

# Create your views here.
@login_required
def home_view(request):
    return render(request, 'home/home.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next') or request.GET.get('next') or 'home'
            return redirect(next_url)
        else:
            error = "Invalid Credentials."
            return render(request, 'accounts/login.html', {"error": error})
    return render(request, 'accounts/login.html')

@login_required
def stocks_view(request):
    return render(request, 'home/stocks.html')

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")
    else:
        return redirect('home')

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = str(form.cleaned_data.get("username"))
            password = form.cleaned_data.get("password")
            user = User.objects.create_user(username, password=password)
            login(request, user)
            return redirect("home")
        else:
            return render(request, 'accounts/register.html', {"form": form})
    return render(request, 'accounts/register.html', {"form": RegisterForm(request.POST)})