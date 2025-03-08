from urllib import response
from django.shortcuts import redirect, render
from httpx import options
import pdfkit
from .models import Profile
from .forms import ProfileForm
from django.urls import reverse
from django.http import HttpResponse
from django.template import loader
import io
from django.contrib import messages
# Create your views here.

def home(request):
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.education_point = [i.strip() for i in profile.education.split(",")]
            profile.work_experience_point = [i.strip() for i in profile.work_experience.split(",")]
            profile.technical_skills_point = [i.strip() for i in profile.technical_skills.split(",")]
            profile.soft_skills_point = [i.strip() for i in profile.soft_skills.split(",")]
            profile.certifications_point = [i.strip() for i in profile.certifications.split(",")]
            profile.languages_point = [i.strip() for i in profile.languages.split(",")]
            profile.additional_training_point = [i.strip() for i in profile.additional_training.split(",")]
            profile.projects_point = [i.strip() for i in profile.projects.split(",")]
            profile.volunteer_experience_point = [i.strip() for i in profile.volunteer_experience.split(",")]
            profile.save()
            return redirect('profile')
    else:
        form = ProfileForm()
        
    return render(request,'index.html',{"form":form})

def profile(request):
    profiles = Profile.objects.all()
    return render(request,'profile.html',{"profiles":profiles})

def edit(request,pk):
    profile = Profile.objects.get(id=pk)
    if request.method == "POST":
        form = ProfileForm(request.POST,instance = profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.education_point = [i.strip() for i in profile.education.split(",")]
            profile.work_experience_point = [i.strip() for i in profile.work_experience.split(",")]
            profile.technical_skills_point = [i.strip() for i in profile.technical_skills.split(",")]
            profile.soft_skills_point = [i.strip() for i in profile.soft_skills.split(",")]
            profile.certifications_point = [i.strip() for i in profile.certifications.split(",")]
            profile.languages_point = [i.strip() for i in profile.languages.split(",")]
            profile.additional_training_point = [i.strip() for i in profile.additional_training.split(",")]
            profile.projects_point = [i.strip() for i in profile.projects.split(",")]
            profile.volunteer_experience_point = [i.strip() for i in profile.volunteer_experience.split(",")]
            profile.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance = profile)
        
    return render(request,'index.html',{"form":form})

def generate(request,pk):
    profile = Profile.objects.get(id=pk)
    name = profile.full_name
    template = loader.get_template('resume.html')
    html = template.render({"profile":profile})
    options = {
        'page-size':'Letter',
        'encoding':'UTF-8', 
    }
    config = pdfkit.configuration(wkhtmltopdf=r"C:\Users\rc120\Downloads\wkhtmltox-0.12.6-1.mxe-cross-win64\wkhtmltox\bin\wkhtmltopdf.exe")
    pdf = pdfkit.from_string(html,False,options,configuration=config)
    response = HttpResponse(pdf,content_type="application/pdf")
    filename = f'{name}-resume.pdf'
    # response['Content-Disposition'] ='attachment'
    return response

def delete(request,pk):
    profile = Profile.objects.get(id = pk)
    profile.delete()
    messages.success(request,"Profile has been deleted successfully !!")
    return redirect(reverse("profile"))
        
        