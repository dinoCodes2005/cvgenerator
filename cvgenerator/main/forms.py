from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ('education_point','work_experience_point','technical_skills_point','soft_skills_point','certifications_point','languages_point','additional_training_point','projects_point','volunteer_experience_point')
        widgets = {
            'full_name': forms.TextInput(attrs={
                'placeholder': 'Enter your full name',
                'class': 'block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm'
            }),
            'address': forms.TextInput(attrs={
                'placeholder': 'Enter your address',
                'class': 'block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm'
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Enter your phone number',
                'class': 'block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm'
            }),
            'linkedin_profile': forms.URLInput(attrs={
                'placeholder': 'Enter your LinkedIn profile URL',
                'class': 'block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm'
            }),
            'personal_statement': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Write a brief personal statement',
                'class': 'block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm'
            }),
            'education': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Enter your education details separated by comma',
                'class': 'block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm'
            }),
            'work_experience': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Describe your work experience separated by comma',
                'class': 'block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm'
            }),
            'technical_skills': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'List your technical skills separated by comman',
                'class': 'block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm'
            }),
            'soft_skills': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'List your soft skills (optional) separated by comma',
                'class': 'block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm'
            }),
            'certifications': forms.Textarea(attrs={
                'rows':3,
                'class': 'block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 focus:outline-none',
                'placeholder':'Enter your certifications',
            }),
            'languages': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'List languages you know (optional) separated by comma',
                'class': 'block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm'
            }),
            'additional_training': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Describe any additional training (optional) separated by comma',
                'class': 'block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm'
            }),
            'projects': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'List your projects separated by comma',
                'class': 'block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm'
            }),
            'volunteer_experience': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Describe your volunteer experience (optional) separated by comma',
                'class': 'block w-full rounded-md bg-white px-3 py-1.5 text-base text-gray-900 outline-1 outline-gray-300 placeholder:text-gray-400 focus:outline-2 focus:-outline-offset-2 focus:outline-indigo-600 sm:text-sm'
            }),
        }
