from django.db import models
from ckeditor.fields import RichTextField

from core.models import Image
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200)
    desciption = RichTextField()
    seo_text = models.TextField()
    is_active = models.BooleanField(default=False)
    publish_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(null=True, blank=True)
    is_draft = models.BooleanField(default=True)
    images = models.ForeignKey(Image, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)
