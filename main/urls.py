from django.urls import path
from . import views

urlpatterns = [
    path('badges/', views.BadgesList.as_view()),
    path('certifications/', views.CertificationsList.as_view()),
    path('projects/', views.ProjectsList.as_view()),
]
