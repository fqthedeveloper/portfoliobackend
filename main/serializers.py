from rest_framework import serializers
from . import models


class BadgesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.badges
        fields = ['id','title','badges','alt_text']


class CertificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.certifications
        fields = ['id','title','certifications','alt_text']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.project
        fields = ['id','title','project','alt_text','description','ghLink','demoLink']