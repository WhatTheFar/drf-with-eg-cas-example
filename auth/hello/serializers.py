from rest_framework import serializers

from hello.models import Auth


class AuthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auth
        fields = ('id', 'name',)
