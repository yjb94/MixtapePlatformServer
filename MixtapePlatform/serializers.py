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

    # sequence = serializers.IntegerField(read_only=True)
    # email = serializers.EmailField(required=True, allow_blank=False, allow_null=False, max_length=100)
    # password = serializers.CharField(max_length=100)
    # profile_url = serializers.URLField(max_length=100)
    # thumbnail_url = serializers.URLField(max_length=100)
    # nickname = serializers.CharField(max_length=12)
    #
    # def create(self, validated_data):
    #     return User.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.email = validated_data.get('email',instance.email)
    #     instance.password = validated_data.get('password',instance.password)
    #     instance.profile_url = validated_data.get('profile_url',instance.profile_url)
    #     instance.thumbnail_url = validated_data.get('thumbnail_url',instance.thumbnail_url)
    #     instance.nickname = validated_data.get('nickname',instance.nickname)
    #     instance.save()
    #     return instance