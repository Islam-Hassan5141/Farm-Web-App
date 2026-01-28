from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm
from .models import Head

# Create your views here.
@login_required
def home_view(request):
    username = request.user.get_username()
    return render(request, 'home/home.html', {'username': username, 'user': request.user})

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
    query = request.GET.get('q')
    sale_status = request.GET.get('sale_status')
    heads = Head.objects.all()
    
    if query:
        heads = heads.filter(animal__icontains=query)

    if sale_status == '1':
        heads = heads.filter(ready_for_sale=True)
    elif sale_status == '0':
        heads = heads.filter(ready_for_sale=False)

    return render(request, 'home/stocks.html', {"heads": heads})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")
    else:
        return render(request, "accounts/logout.html")

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

@login_required
def shipping_view(request):
    return render(request, 'home/shipping.html')

def about_view(request):
    return render(request, 'home/about.html')    