from django.shortcuts import render, get_object_or_404
from .models import ProfileInfo, Project

def home_view(request):
    profile = ProfileInfo.objects.first()
    return render(request, 'core/home.html', {"profile":profile})

def project_list_view(request):
    projects = Project.objects.filter(is_published=True).order_by('order')
    return render(request, 'core/project_list.html', {"projects":projects})

def project_detail_view(request, slug):
    project = get_object_or_404(Project, slug=slug, is_published=True)
    return render(request, 'core/project_detail.html', {"project":project})