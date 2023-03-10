from rest_framework import viewsets

from .models import PassHolder
from .serializers import PassHolderSerializer


class PassHolderViewSet(viewsets.ModelViewSet):
    queryset = PassHolder.objects.all()
    serializer_class = PassHolderSerializer

    def perform_destroy(self, instance):
        super(PassHolderViewSet, self).perform_destroy(instance)
