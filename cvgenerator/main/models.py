from django.db import models

# Create your models here.
class Profile(models.Model):
    
    full_name = models.CharField(max_length=200,blank=False)
    address = models.CharField(max_length=255, blank=False)
    phone_number = models.CharField(max_length=20, blank=False)
    linkedin_profile = models.URLField(max_length=200, blank=False)
    personal_statement = models.CharField(max_length=300,blank=False)
    
    education = models.TextField(blank=False)
    education_point = models.JSONField(default = list)
    
    work_experience = models.TextField(blank=False)
    work_experience_point = models.JSONField(default=list)
    
    technical_skills = models.TextField(blank=False)
    technical_skills_point = models.JSONField(default=list)
    
    soft_skills = models.TextField(blank=True)
    soft_skills_point = models.JSONField(default=list)
    
    certifications = models.TextField(max_length=200,blank=True)
    certifications_point = models.JSONField(default=list)
    
    languages = models.TextField(blank=True)
    languages_point = models.JSONField(default=list)
    
    additional_training = models.TextField(blank=True)
    additional_training_point = models.JSONField(default=list)

    projects = models.TextField(blank=True)
    projects_point = models.JSONField(default=list)
    
    volunteer_experience = models.TextField(blank=True)
    volunteer_experience_point = models.JSONField(default=list)

    def __str__(self):
        return self.full_name
    