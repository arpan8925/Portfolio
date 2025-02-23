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
    context = {
        'project': project
    }
    return render(request,'project-details.html', context)

def projects(request):
    return render(request,'project.html')

def contact(request):
    return render(request,'contact.html')