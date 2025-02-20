from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def project_details(request):
    return render(request,'project-details.html')

def contact(request):
    return render(request,'contact.html')