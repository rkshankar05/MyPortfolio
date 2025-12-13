from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import About, Experience, ExperienceDetail, TechStack

class ExperienceDetailInline(admin.TabularInline):
    model = ExperienceDetail
    extra = 3
    fields = ['description', 'order']

class TechStackInline(admin.TabularInline):
    model = TechStack
    extra = 3
    fields = ['technology', 'order']

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'phone']
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'title', 'bio', 'profile_image')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'location')
        }),
        ('Social Links', {
            'fields': ('linkedin', 'github', 'twitter')
        }),
    )

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'organization','project_link','order']
    list_editable = ['order']
    prepopulated_fields = {'slug': ('project_name',)}
    inlines = [ExperienceDetailInline, TechStackInline]
    fieldsets = (
        ('Project Information', {
            'fields': ('project_name', 'organization','project_link', 'slug')
        }),
        ('Display Order', {
            'fields': ('order',),
            'description': 'Higher number appears first on the page'
        }),
    )