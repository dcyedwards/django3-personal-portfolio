from django.shortcuts import render
from .models import Project


# Create your views here.

def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/portfolio_home.html', {'Person': 'Ebenezer',

                                                             'projects': projects})


def about(request):
    return render(request, 'portfolio/about.html')
