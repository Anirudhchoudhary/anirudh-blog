from rest_framework import serializers
from core.models import Image

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ['id', 'title', 'description', 'seo_text', 'created_at', 'images']
