from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from wallpapers_app.models import Wallpaper, Category
from wallpapers_app.forms import CategoryForm
# Pagination
from django.core.paginator import Paginator
# Messages
from django.contrib import messages

@staff_member_required
def contributions(request):
    if request.method == 'POST':
        wallpaper_id = request.POST.get('wallpaper_id')
        value = request.POST.get('published')

        wallpaper = get_object_or_404(Wallpaper, pk=wallpaper_id)

        if value == 'True':
            wallpaper.published = True
            wallpaper.save()
        elif value == 'False':
            wallpaper.delete()
        
        return redirect('contributions')
    
    wallpaper_list = Wallpaper.objects.all().order_by('published', '-created_at')

    to_approve_count = wallpaper_list.filter(published = False).count()
    approved_count = wallpaper_list.filter(published = True).count()
    total_count = approved_count + to_approve_count
    
    # Set up Pagination
    p = Paginator(wallpaper_list, 15)
    page = request.GET.get('page')
    wallpapers = p.get_page(page)

    return render(request, 'contributions.html', {'wallpapers': wallpapers, 'approved_count':approved_count, 'to_approve_count':to_approve_count, 'total_count':total_count})


@staff_member_required
def categories(request):
    category_list = Category.objects.all().order_by('name')
    total_count = category_list.count()
    
    # Set up Pagination
    p = Paginator(category_list, 15)
    page = request.GET.get('page')
    categories = p.get_page(page)

    return render(request, 'categories/categories.html', {'categories': categories, 'total_count':total_count})


@staff_member_required
def category_create(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            messages.success(request, ('La categoria ha sido creada con exito.'))
            return redirect('/admin-wallpapers/categories')
    else:
        form = CategoryForm()
    
    return render(request, 'categories/categories-edit.html', {'form':form})

@staff_member_required
def category_edit(request, id):
    category = get_object_or_404(Category, pk=id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            messages.success(request, ('La categoria ha sido modificada con exito.'))
            return redirect('/admin-wallpapers/categories')
    else:
        form = CategoryForm(instance=category)

    return render(request, 'categories/categories-edit.html', {'form':form})


@staff_member_required
def category_delete(request, id):
    category = get_object_or_404(Category, pk=id)
    category.delete()
    messages.success(request, ('La categoria ha sido borrada con exito.'))
    return redirect('/admin-wallpapers/categories')