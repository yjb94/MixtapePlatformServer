from rest_framework import serializers
from MixtapePlatform.models import *
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('sequence','email','password','profile_url','thumbnail_url','nickname')

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def create(self, validated_data):
        user = User.objects.create(**validated_data)
        return user

    def delete(self, pk):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AudioSerializer(serializers.ModelSerializer):
    pass