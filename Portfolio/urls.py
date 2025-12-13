from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('experience/', views.experience_list, name='Experience'),
    path('experience/<slug:slug>/', views.experience_detail, name='experience_detail'),
]