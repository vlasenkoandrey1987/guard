from datetime import datetime

from rest_framework import serializers

from .models import Pass, PassHolder


class PassHolderSerializer(serializers.ModelSerializer):

    class Meta:
        model = PassHolder
        fields = ('id', 'person', 'photo')


class PassSerializer(serializers.ModelSerializer):
    mfuid = serializers.CharField(read_only=True)
    active = serializers.SerializerMethodField()

    class Meta:
        model = Pass
        fields = ('id', 'pass_holder', 'mfuid', 'valid_from', 'valid_until',
                  'active', 'created')

    def get_active(self, instance):
        return (instance.valid_from <= datetime.now().astimezone() <
                instance.valid_until)
