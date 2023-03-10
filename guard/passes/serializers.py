from rest_framework import serializers

from .models import PassHolder


class PassHolderSerializer(serializers.ModelSerializer):

    class Meta:
        model = PassHolder
        fields = ('id', 'person', 'photo')
