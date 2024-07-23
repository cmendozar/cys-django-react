from django.shortcuts import render
from .models import Project

# Create your views here.

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'realestate/project_list.html', {'projects': projects})

