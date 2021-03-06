from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm


def signUpView(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account successfully created ' + user)
            return redirect('accounts:login')

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def loginView(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('app:home')
        else:
            messages.info(
                request, 'username and password are case sensitive and/or password and username did not match')

    return render(request, 'accounts/login.html')


def logoutView(request):
    logout(request)
    return redirect('accounts:login')
