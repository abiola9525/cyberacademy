from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'users/home.html')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('preview')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required()
def profile(request):
    return render(request, 'users/profile.html')

@login_required()
def preview(request):
    return render(request, 'users/preview.html')

@login_required()
def intro(request):
    return render(request, 'users/intro.html')

@login_required()
def lesson1(request):
    return render(request, 'users/lesson1.html')

@login_required()
def lesson2(request):
    return render(request, 'users/lesson2.html')

@login_required()
def lesson3(request):
    return render(request, 'users/lesson3.html')

@login_required()
def lesson4(request):
    return render(request, 'users/lesson4.html')

@login_required()
def lesson5(request):
    return render(request, 'users/lesson5.html')

@login_required()
def lesson6(request):
    return render(request, 'users/lesson6.html')

@login_required()
def lesson7(request):
    return render(request, 'users/lesson7.html')

@login_required()
def lesson8(request):
    return render(request, 'users/lesson8.html')

@login_required()
def lesson9(request):
    return render(request, 'users/lesson9.html')

@login_required()
def lesson10(request):
    return render(request, 'users/lesson10.html')

@login_required()
def lesson11(request):
    return render(request, 'users/lesson11.html')

@login_required()
def lesson12(request):
    return render(request, 'users/lesson12.html')

@login_required()
def lesson13(request):
    return render(request, 'users/lesson13.html')



