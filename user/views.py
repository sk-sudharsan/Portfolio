import os

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def home(request):
    personal_details = PersonalDetails.objects.first()
    skills = Skills.objects.all()
    education = Education.objects.order_by('-graduation_year')
    projects = Project.objects.all()
    experience = Experience.objects.order_by('-year')
    context = {
        'personal_details': personal_details,
        'skills': skills,
        'education': education,
        'projects': projects,
        'experience': experience
    }
    return render(request,'index.html', context)

def viewcv(request):
    cv = resume.objects.first()
    context = {
        'image':cv
    }
    return render(request, 'resume.html', context)



def download_resume(request):
    Resume = get_object_or_404(resume)
    resume_path = Resume.cv.path
    with open(resume_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename=' + os.path.basename(resume_path)
        return response
