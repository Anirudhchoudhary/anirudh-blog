from django.db import models
from ckeditor.fields import RichTextField

from core.models import Image
# Create your models here.

class NewsManager(models.Manager):
    def get_queryset(self):
        return super(NewsManager, self).get_queryset().filter(is_news=True, is_active=True)


class PostManager(models.Manager):
    def get_queryset(self):
        return super(PostManager, self).get_queryset().filter(is_news=False, is_active=True)


class CompleteManager(models.Manager):
    def get_queryset(self):
        return super(CompleteManager, self).get_queryset()

class Post(models.Model):
    title = models.CharField(max_length=200)
    desciption = RichTextField()
    seo_text = models.TextField()
    is_news = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    publish_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(null=True, blank=True)
    is_draft = models.BooleanField(default=True)
    images = models.ForeignKey(Image, null=True, on_delete=models.CASCADE)

    newsobject = NewsManager()
    postobject = PostManager()
    objects = CompleteManager()

    def __str__(self):
        return str(self.title)

    @property
    def liked(self):
        try:
            return self.poststats_set.all().first().like
        except:
            return 0

    @property
    def viewed(self):
        try:
            return self.poststats_set.all().first().viewed
        except:
            return 0

class PostStats(models.Model):
    like = models.PositiveIntegerField(default=0)
    viewed = models.PositiveIntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.like)

