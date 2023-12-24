from django.shortcuts import render, redirect
from .forms import RegisterForm, WallpaperForm, CommentForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import Wallpaper, Category, Comment
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
# Pagination
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    latest = Wallpaper.objects.all().filter(published=True).order_by('-created_at')[:12]
    popular = Wallpaper.objects.all().filter(published=True).order_by('-download_count')[:12]

    return render(request, 'main/home.html', {'latest': latest, 'popular':popular})

def wallpaper_list(request):
    category_id = request.GET.get('category', 0)
    order_by = request.GET.get('order_by', '-created_at')

    wallpaper_list = Wallpaper.objects.all().filter(published=True).order_by(order_by)

    if category_id != 0:
        wallpaper_list = wallpaper_list.filter(category__id=category_id)

    category_list = Category.objects.all().order_by('name')

    # Set up Pagination
    p = Paginator(wallpaper_list, 20)
    page = request.GET.get('page')
    wallpapers = p.get_page(page)

    return render(request, 'main/wallpaper_list.html', {'wallpapers': wallpapers, 'categories': category_list})

def wallpaper_list_search(request):
    if request.method == "POST":
        searched = request.POST['searched']

        wallpaper_list = Wallpaper.objects.filter(title__icontains=searched).order_by('-created_at')
        category_list = Category.objects.all().order_by('name')

        # Set up Pagination
        p = Paginator(wallpaper_list, 20)
        page = request.GET.get('page')
        wallpapers = p.get_page(page)

        return render(request, 'main/wallpaper_list.html', {'wallpapers': wallpapers, 'categories': category_list, 'searched': searched })
    
    return HttpResponseNotFound()  

def wallpaper(request, id):
    item = Wallpaper.objects.get(id=id)
    comments = Comment.objects.all().filter(wallpaper=item)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.wallpaper = item
            comment.author = request.user
            comment.save()
            return redirect("/wallpaper/" + str(item.id))
    else:
        form = CommentForm()

    return render(request, 'main/wallpaper_item.html',{'item':item, 'comments':comments, "form": form})

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

@login_required(login_url="/login")
def create_comment(request, id):
    wallpaper = get_object_or_404(Wallpaper, id=id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.wallpaper = wallpaper
            comment.author = request.user
            comment.save()
            return redirect("/wallpaper/" + wallpaper.id)
    else:
        form = CommentForm()

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
