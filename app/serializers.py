import os
from PIL import Image
from django.conf import settings
from rest_framework import serializers
from . import models


class CatSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api-cat-detail')

    class Meta:
        model = models.Cat
        fields = [
            'id', 'url', 'cover', 'name', 'description',
            'history', 'breed', 'is_special'
        ]

    def save(self, **kwargs):
        cat = super().save(**kwargs)

        if cat.cover:
            self.resize_image(cat.cover, 800, 800)

        cat.save()
        return cat

    @staticmethod
    def resize_image(image, new_width=800, new_height=None):
        image_full_path = os.path.join(settings.MEDIA_URL, image.path)
        image_pillow = Image.open(image_full_path)
        original_width, original_height = image_pillow.size

        if original_width <= new_width:
            image_pillow.close()
            return

        if new_height is None:
            new_height = round((new_width * original_height) / original_width)

        new_image = image_pillow.resize((new_width, new_height), Image.LANCZOS)
        new_image.save(
            image_full_path,
            optimize=True,
            quality=50,
        )
