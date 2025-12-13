from django.shortcuts import render, get_object_or_404
from .models import About, Experience

def home(request):
    about = About.objects.first()
    
    # Clear the profile_image if it causes issues
    if about and about.profile_image:
        try:
            # Test if the file exists
            about.profile_image.url
        except:
            about.profile_image = None
    
    context = {
        'about': about,
    }
    return render(request, 'Portfolio/home.html', context)
    
def experience_list(request):
    about = About.objects.first()
    experiences = Experience.objects.all()
    context = {
        'experiences': experiences,
        'about': about,
    }
    return render(request, 'Portfolio/Experience.html', context)

def experience_detail(request, slug):
    about = About.objects.first()
    experience = get_object_or_404(Experience, slug=slug)
    context = {
        'experience': experience,
        'about': about,
    }
    return render(request, 'Portfolio/experience_detail.html', context)