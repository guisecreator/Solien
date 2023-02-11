from django.contrib import admin
from .models import Task
from django.contrib import admin
from .models import Profiles

admin.site.register(Task)


@admin.register(Profiles)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth']