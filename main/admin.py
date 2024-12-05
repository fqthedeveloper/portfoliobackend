from django.contrib import admin
from . import models


class BadgesAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag', 'alt_text')
admin.site.register(models.badges, BadgesAdmin)

class CertificationsAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag', 'alt_text')
admin.site.register(models.certifications, CertificationsAdmin)

class ParojectsAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag', 'description')
admin.site.register(models.project, ParojectsAdmin)