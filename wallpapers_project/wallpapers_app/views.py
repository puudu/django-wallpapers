from django.shortcuts import render, redirect
from .forms import RegisterForm, WallpaperForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Wallpaper, Category
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

# Pagination
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def wallpaper_list(request):
    category_id = request.GET.get('category', 0)
    order_by = request.GET.get('order_by', '-created_at')

    wallpaper_list = Wallpaper.objects.all().order_by(order_by)

    if category_id != 0:
        wallpaper_list = wallpaper_list.filter(category__id=category_id)

    category_list = Category.objects.all().order_by('name')

    # Set up Pagination
    p = Paginator(wallpaper_list, 20)
    page = request.GET.get('page')
    wallpapers = p.get_page(page)

    return render(request, 'main/wallpaper_list.html', {'wallpapers': wallpapers, 'categories': category_list})

def wallpaper(request, id):
    item = Wallpaper.objects.get(id=id)

    return render(request, 'main/wallpaper_item.html',{'item':item})

def increment_download_count(request, wallpaper_id):
    wallpaper = get_object_or_404(Wallpaper, pk=wallpaper_id)
    wallpaper.increment_download_count()
    wallpaper.save()
    print('download count incremented')
    return HttpResponse('')

@login_required(login_url="/login")
def create_contribution(request):
    if request.method == 'POST':
        form = WallpaperForm(request.POST, request.FILES)
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
