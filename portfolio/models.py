from django.db import models
from django.utils.text import slugify

class About(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=200, default="India")
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    twitter = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = "About"

    def __str__(self):
        return self.name


class Experience(models.Model):
    project_name = models.CharField(max_length=200)
    organization = models.CharField(max_length=200, blank=True)
    project_link = models.URLField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['-order']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.project_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.project_name


class ExperienceDetail(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='details')
    description = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.description[:50]


class TechStack(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='tech_stack')
    technology = models.CharField(max_length=100)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.technology