from rest_framework import serializers

from .models import Pass, PassHolder


class PassHolderSerializer(serializers.ModelSerializer):

    class Meta:
        model = PassHolder
        fields = ('id', 'person', 'photo')


class PassSerializer(serializers.ModelSerializer):
    mfuid = serializers.CharField(read_only=True)

    # Реализовать поле active

    class Meta:
        model = Pass
        fields = ('id', 'pass_holder', 'mfuid', 'valid_from', 'valid_until',
                  'created')
