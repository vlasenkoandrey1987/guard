from datetime import datetime

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
        for pass_ in instance.passes.all():
            if (pass_.valid_from <= datetime.now().astimezone() <
                    pass_.valid_until):
                raise PermissionDenied
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
        if ('mfuid' in self.request.data
                and self.request.data['mfuid'] != serializer.instance.mfuid):
            raise PermissionDenied
        super(PassViewSet, self).perform_update(serializer)
