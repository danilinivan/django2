from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import SignInForm, SignUpForm

def sign_up(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('users:sign_in')
    form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})    


def sign_in(request):
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('blog:home')
    form = SignInForm()
    return render(request, 'sign_in.html', {'form': form})    


def sign_out(request):
    logout(request)
    return redirect('users:sign_in')