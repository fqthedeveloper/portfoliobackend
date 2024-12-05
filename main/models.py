from django.db import models
from django.utils.html import mark_safe

# Create your models here.

class badges(models.Model):
    title = models.CharField(max_length=500)
    badges = models.ImageField(upload_to="badges/")
    alt_text = models.CharField(max_length=500)

    class Meta :
        verbose_name_plural = 'Badges'

    def __str__(self) :
        return self.title

    def image_tag(self) :
        return mark_safe('<img src="%s" width="80" />' % (self.badges.url))
    

class certifications(models.Model):
    title = models.CharField(max_length=500)
    certifications = models.ImageField(upload_to="certifications/")
    alt_text = models.CharField(max_length=500)

    class Meta :
        verbose_name_plural = 'Certification'

    def __str__(self) :
        return self.title

    def image_tag(self) :
        return mark_safe('<img src="%s" width="80" />' % (self.certifications.url))
    

class project(models.Model):
    title = models.CharField(max_length=500)
    project = models.ImageField(upload_to="project/")
    alt_text = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    ghLink = models.CharField(max_length=500)
    demoLink = models.CharField(max_length=500)


    class Meta :
        verbose_name_plural = 'Project'

    def __str__(self) :
        return self.title

    def image_tag(self) :
        return mark_safe('<img src="%s" width="80" />' % (self.project.url))