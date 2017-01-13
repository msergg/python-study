from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate

from django.urls.base import reverse
from .forms import LoginForm


def logout_(request):
    logout(request)
    return redirect(reverse('index'))


def login_(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            passwd = form.cleaned_data['passwd']

            user = authenticate(username=username, password=passwd)
            if user is not None:
                login(request,user)
                return redirect(reverse('index'))



    return render(request, 'login.html', {'form':form})






