from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest

import blog.models as models
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    """
    Post admin
    """

    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return models.Post.objects.all()


admin.site.register(models.Post, PostAdmin)