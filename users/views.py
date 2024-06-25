from django.contrib.auth import authenticate, login, get_user_model, logout
from django.shortcuts import render, redirect

from users.forms import LoginForm, RegisterForm
from users.models import User


# Create your views here.
def login_view(request):
    # if request.user.is_authenticated:
    #     return redirect('/')
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        user_name = form.cleaned_data.get('user_name')
        password = form.cleaned_data.get('password')
        User = get_user_model()
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            query = request.GET.get('next')
            if query is not None:
                return redirect(query)
            else:
                return redirect('/')
        else:
            form.add_error('user_name', 'نام کاربری یا رمز عبور اشتباه است')

    return render(request, 'users/login.html', context)


def logout_view(request):
    logout(request)
    return redirect("login")


def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user_name = form.cleaned_data.get('user_name')
        print(user_name)
        password = form.cleaned_data.get('password')
        print(password)
        email = form.cleaned_data.get('email')
        print(email)
        if email is not None:
            user = User.objects.create_user(username=user_name, password=password, email=email)
        else:
            user = User.objects.create_user(username=user_name, password=password)
        user.save()
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)
