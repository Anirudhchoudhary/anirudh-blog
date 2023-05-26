import sys

from io import BytesIO  #basic input/output operation
from PIL import Image as image_open #Imported to compress images

from django.db import models
from django.core.files.uploadedfile import InMemoryUploadedFile


# Create your models here.
class Image(models.Model):
    img256 = models.ImageField(upload_to="upload/", null=True, blank=True)
    img126 = models.ImageField(upload_to="upload/", null=True, blank=True)
    img512 = models.ImageField(upload_to="upload/")
    name = models.CharField(max_length=123, null=True, blank=True)
    seo_context = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return str(self.name)

    @staticmethod
    def compress_image(size, image, quality):
        imageTemproary = image_open.open(image)
        outputIoStream = BytesIO()
        imageTemproaryResized = imageTemproary.resize( (size,size))
        imageTemproary.save(outputIoStream , format='PNG', quality=quality)
        outputIoStream.seek(0)
        image = InMemoryUploadedFile(outputIoStream,'ImageField', "%s.png" % image.name.split('.')[0], 'image/png', sys.getsizeof(outputIoStream), None)
        return image

    def save(self, *args, **kwargs) -> None:
        self.img126 = self.compress_image(126, self.img512, 50)
        self.img256 = self.compress_image(256, self.img512, 70)
        self.name = self.img512.name
        return super(Image, self).save(*args, **kwargs)
