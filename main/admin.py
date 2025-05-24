from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Experience, Education, Profile

admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Profile)
