from .forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


def login_page(request):
    if request.user.is_authenticated:
        return redirect(to=home_page)
    form = LoginForm(request.POST or None)
    context = {
        'form': form,
        'error': '',
    }
    if form.is_valid():
        userName = form.cleaned_data.get('userName')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=userName, password=password)
        if user is not None:
            login(request, user)
            context['form'] = LoginForm()
            return redirect(to=home_page)
        else:
            context['error'] = 'incorrect username or password'

    return render(request, "login.html", context)


@login_required(login_url=login_page)
def home_page(request):

    return render(request, 'home_page.html', {})


@login_required(login_url=login_page)
def user_profile(request):

    return render(request, 'user_profile.html', {})


@login_required(login_url=login_page)
def users_list(request):

    return render(request, 'users.html', {})


@login_required(login_url=login_page)
def teams_list(request):

    return render(request, 'groups.html', {})


@login_required(login_url=login_page)
def project_list(request):

    return render(request, 'projects.html', {})
