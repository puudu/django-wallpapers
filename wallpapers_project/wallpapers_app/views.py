from django.shortcuts import render, redirect
from .forms import RegisterForm, WallpaperForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'main/home.html')

@login_required(login_url="/login")
def create_contribution(request):
    if request.method == 'POST':
        form = WallpaperForm(request.POST)
        if form.is_valid():
            wallpaper = form.save(commit=False)
            wallpaper.author = request.user
            wallpaper.published = False
            wallpaper.download_count = 0
            wallpaper.save()
            return redirect("/home")
    else:
        form = WallpaperForm()

    return render(request, 'main/create_contribution.html', {"form": form})

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()

    return render(request, 'registration/sign_up.html', {"form": form})