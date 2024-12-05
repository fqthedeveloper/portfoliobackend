from .serializers import BadgesSerializer, CertificationsSerializer, ProjectSerializer
from rest_framework import generics
from rest_framework import permissions
from . import models


# Create your views here.


class BadgesList(generics.ListAPIView) :
    queryset = models.badges.objects.all()
    serializer_class = BadgesSerializer


class CertificationsList(generics.ListAPIView) :
    queryset = models.certifications.objects.all()
    serializer_class = CertificationsSerializer


class ProjectsList(generics.ListAPIView) :
    queryset = models.project.objects.all()
    serializer_class = ProjectSerializer