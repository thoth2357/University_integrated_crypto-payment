from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib import messages


# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html")

def logout_view(request):
    auth.logout(request)
    return redirect('homepage')

def login_view(request, *args, **kwargs):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(username = email, password = password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('student-dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('loginpage')
    return render(request, 'login.html')

def profile_view(request, *args, **kwargs):
    return render(request, "student-dashboard.html")