from django.shortcuts import render, get_object_or_404
from .models import Project


def index(request):
    projects = Project.objects.all().filter(is_featured=True)
    context = {
        'projects': projects
    }
    return render(request,'index.html' , context)

def project_details(request, slug):
    project = get_object_or_404(Project, slug=slug)
    ProjectImages = project.carousel_images.all()
    context = {
        'project': project,
        'projectimages': ProjectImages
    }
    return render(request,'project-details.html', context)

def projects(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request,'project.html', context)

def contact(request):
    return render(request,'contact.html')