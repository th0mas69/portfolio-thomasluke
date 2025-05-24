from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Experience, Education, Profile

def home(request):
    profile = Profile.objects.first()
    experiences = Experience.objects.all()
    education = Education.objects.all()
    return render(request, 'main/home.html', {
        'profile': profile,
        'experiences': experiences,
        'education': education,
    })
