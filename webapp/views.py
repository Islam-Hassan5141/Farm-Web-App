from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'home/home.html')

def login_view(request):
    return render(request, 'registration/login.html')

def stocks_view(request):
    return render(request, 'home/stocks.html')

def logout_view(request):
    return render(request, 'registration/logout.html')

def register_view(request):
    return render(request, 'registration/register.html')