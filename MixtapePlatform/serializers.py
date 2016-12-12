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
            return self.Meta.model.objects.get(sequence=pk)
        except self.Meta.model.DoesNotExist:
            raise Response(status=status.HTTP_400_BAD_REQUEST)

    def create(self, validated_data):
        obj = self.Meta.model.objects.create(**validated_data)
        return obj

    def delete(self, pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLike
        fields = ('sequence', 'user_fk', 'audio_fk')

    def get_object(self, pk):
        try:
            return self.Meta.model.objects.get(sequence=pk)
        except self.Meta.model.DoesNotExist:
            raise Response(status=status.HTTP_400_BAD_REQUEST)

    def create(self, validated_data):
        obj = self.Meta.model.objects.create(**validated_data)
        return obj

    def delete(self, pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserFollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollow
        fields = ('sequence', 'user_fk', 'artist_fk')

    def get_object(self, pk):
        try:
            return self.Meta.model.objects.get(sequence=pk)
        except self.Meta.model.DoesNotExist:
            raise Response(status=status.HTTP_400_BAD_REQUEST)

    def create(self, validated_data):
        obj = self.Meta.model.objects.create(**validated_data)
        return obj

    def delete(self, pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ArtistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Artist
        fields = ('sequence','user_info_fk','aka')

    def get_object(self, pk):
        try:
            return self.Meta.model.objects.get(sequence=pk)
        except self.Meta.model.DoesNotExist:
            raise Response(status=status.HTTP_400_BAD_REQUEST)

    def create(self, validated_data):
        obj = self.Meta.model.objects.create(**validated_data)
        return obj

    def delete(self, pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Audio
        fields = ('sequence','stream_url','artwork_url','waveform_url','description')

    def get_object(self, pk):
        try:
            return self.Meta.model.objects.get(sequence=pk)
        except self.Meta.model.DoesNotExist:
            raise Response(status=status.HTTP_400_BAD_REQUEST)

    def create(self, validated_data):
        obj = self.Meta.model.objects.create(**validated_data)
        return obj

    def delete(self, pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class BeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Beat
        fields = ('sequence','audio_info_fk','sc_id','audio_info')

    def get_object(self, pk):
        try:
            return self.Meta.model.objects.get(sequence=pk)
        except self.Meta.model.DoesNotExist:
            raise Response(status=status.HTTP_400_BAD_REQUEST)

    def create(self, validated_data):
        obj = self.Meta.model.objects.create(**validated_data)
        return obj

    def delete(self, pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MixtapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mixtape
        fields = ('sequence', 'artist_fk', 'original_beat_fk', 'audio_info_fk', 'voice_url', 'lyrics')

    def get_object(self, pk):
        try:
            return self.Meta.model.objects.get(sequence=pk)
        except self.Meta.model.DoesNotExist:
            raise Response(status=status.HTTP_400_BAD_REQUEST)

    def create(self, validated_data):
        obj = self.Meta.model.objects.create(**validated_data)
        return obj

    def delete(self, pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ChartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chart
        fields = ('sequence', 'chart_type', 'date')

    def get_object(self, pk):
        try:
            return self.Meta.model.objects.get(sequence=pk)
        except self.Meta.model.DoesNotExist:
            raise Response(status=status.HTTP_400_BAD_REQUEST)

    def create(self, validated_data):
        obj = self.Meta.model.objects.create(**validated_data)
        return obj

    def delete(self, pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
