
from django.contrib import admin
from .models import Profile

# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name','address','phone_number')


admin.site.register(Profile,ProfileAdmin)

