import os
from rest_framework import viewsets
from . import models
from . import serializers


class CatViewSets(viewsets.ModelViewSet):
    queryset = models.Cat.objects.all()
    serializer_class = serializers.CatSerializer

    def perform_update(self, serializer):
        if os.path.exists(serializer.instance.cover.path):
            os.remove(serializer.instance.cover.path)
        return super().perform_update(serializer)

    def perform_destroy(self, instance):
        if os.path.exists(instance.cover.path):
            os.remove(instance.cover.path)
        return super().perform_destroy(instance)
