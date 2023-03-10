from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from .models import PassHolder
from .serializers import PassHolderSerializer, PassSerializer
from .utils import create_mfuid


class PassHolderViewSet(viewsets.ModelViewSet):
    queryset = PassHolder.objects.all()
    serializer_class = PassHolderSerializer

    def perform_destroy(self, instance):
        # Реализовать запрет на удаление, если у держателя пропусков есть хоть
        # один активный пропуск
        super(PassHolderViewSet, self).perform_destroy(instance)


class PassViewSet(viewsets.ModelViewSet):
    serializer_class = PassSerializer

    def get_queryset(self):
        pass_holder_id = self.kwargs.get('pass_holder_id')
        pass_holder = get_object_or_404(PassHolder, id=pass_holder_id)
        return pass_holder.passes.all()

    def perform_create(self, serializer):
        serializer.save(mfuid=create_mfuid())

    def perform_update(self, serializer):
        # Дописать запрет на обновление, если mfuid не совпадает с текущим
        super(PassViewSet, self).perform_update(serializer)
