from django.contrib import messages
from django.shortcuts import render, redirect


# /login
def login(request):
    if request.method == 'POST':
        print('SUBMITTED LOG')
        return redirect('login')
    return render(request, 'accounts/login.html')


# /logout
def logout(request):
    return render(request, 'index')


# /dashboard
def dashboard(request):
    return render(request, 'accounts/dasboard.html')


# /register
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password_check = request.POST['password_check']

        # Check if passwords match
        if password == password_check:
            messages.error(request, 'Matches')
        else:
            messages.error(request, 'Password doesnt mtvh')


    else:
        print('SUBMITTED Failed')
        return render(request, 'accounts/register.html')
