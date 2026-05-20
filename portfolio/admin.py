from django.contrib import admin
from .models import About, Experience, ExperienceDetail, TechStack

class ExperienceDetailInline(admin.TabularInline):
    model = ExperienceDetail
    extra = 3

class TechStackInline(admin.TabularInline):
    model = TechStack
    extra = 3

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'phone']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'organization', 'project_link', 'order']
    list_editable = ['order']
    prepopulated_fields = {'slug': ('project_name',)}
    inlines = [ExperienceDetailInline, TechStackInline]