from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from wallpapers_app.models import Wallpaper
# Pagination
from django.core.paginator import Paginator

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