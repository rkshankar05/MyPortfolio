from django.shortcuts import render, get_object_or_404
from .models import About, Experience

def home(request):
    about = About.objects.first()
    return render(request, 'portfolio/home.html', {'about': about})

def experience_list(request):
    about = About.objects.first()
    experiences = Experience.objects.all()
    return render(request, 'portfolio/experience.html', {
        'about': about,
        'experiences': experiences
    })

def experience_detail(request, slug):
    about = About.objects.first()
    experience = get_object_or_404(Experience, slug=slug)
    return render(request, 'portfolio/experience_detail.html', {
        'about': about,
        'experience': experience
    })