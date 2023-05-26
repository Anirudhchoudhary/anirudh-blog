from django.contrib import admin

import core.models as models
# Register your models here.


class ImageAdmin(admin.ModelAdmin):
    list_display = ['img512', 'name']
    fields = ('name', 'img512', 'img126', 'img256')

admin.site.register(models.Image, ImageAdmin)