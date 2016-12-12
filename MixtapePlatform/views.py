from math import radians

from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import serializers, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

import re
from MixtapePlatform.models import *
from MixtapePlatform.serializers import *
# Create your views here.


class UserApi(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self, pk):
        queryset = self.get_queryset()
        obj = queryset.get(sequence=pk)
        return obj


    def get(self, request, *args, **kwargs):
        pk = request.query_params.get('sequence')
        all = request.query_params.get('all')
        if(all is not None and int(all) == 1):
            return Response(self.serializer_class(self.get_queryset(),many=True).data)
        else:
            try:
                user = self.get_object(pk)
                serializer = self.serializer_class(user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        request.data['profile_url'] = "http://placehold.it/300X300"
        request.data['thumbnail_url'] = "http://placehold.it/1600X900"
        aka = re.search("[\w.]+", request.data['email']).group()
        request.data['nickname'] = aka
        serializer = self.serializer_class(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            artist = {}
            artist['user_info_fk'] = serializer.data.get('sequence')
            artist['aka'] = aka
            artist_serializer = ArtistSerializer(data=artist)
            if(artist_serializer.is_valid()):
                artist_serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        pk = request.query_params.get('sequence')
        user = self.get_object(pk)
        serializer = self.serializer_class(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        pk = request.query_params.get('sequence')
        try:
            user = self.get_object(pk)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ArtistApi(GenericAPIView, mixins.ListModelMixin):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    def get(self, request, *args, **kwargs):
        return Response(self.serializer_class(self.get_queryset(), many=True).data)


class ArtistDetailApi(GenericAPIView, mixins.ListModelMixin):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

    def get_object(self, pk):
        queryset = self.get_queryset()
        obj = queryset.get(sequence=pk)
        return obj

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('sequence')
        try:
            artist = self.get_object(pk)
            serializer = self.serializer_class(artist)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class LoginApi(GenericAPIView, mixins.ListModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_object(self, email, password):
        queryset = self.get_queryset()
        obj = queryset.get(email=email, password=password)
        return obj

    def post(self, request, *args   , **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            user = self.get_object(email,password)
            serializer = self.serializer_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class AudioApi(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer

    def get_object(self, pk):
        queryset = self.get_queryset()
        obj = queryset.get(sequence=pk)
        return obj

    def get(self, request, *args, **kwargs):
        return Response(self.serializer_class(self.get_queryset(), many=True).data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

            # artist_fk = request.data.get('artist_fk')
        # artist = Artist.objects.all().get(sequence=artist_fk)
        # if(serializer.is_valid()):
        #     serializer.save(artist_fk=artist)
        #     return Response(serializer.data, status=status.HTTP_200_OK )
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MixtapeApi(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = Mixtape.objects.all()
    serializer_class = MixtapeSerializer

    def get_object(self, pk):
        queryset = self.get_queryset()
        obj = queryset.get(sequence=pk)
        return obj

    def get(self, request, *args, **kwargs):
        return Response(self.serializer_class(self.get_queryset(), many=True).data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

class BeatApi(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = Beat.objects.all()
    serializer_class = BeatSerializer

    def get_object(self, pk):
        queryset = self.get_queryset()
        obj = queryset.get(sequence=pk)
        return obj

    def get(self, request, *args, **kwargs):
        return Response(self.serializer_class(self.get_queryset(), many=True).data  )

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


class AudioDetailApi(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer

    def get_object(self, pk):
        queryset = self.get_queryset()
        obj = queryset.get(sequence=pk)
        return obj

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('sequence')
        try:
            audio = self.get_object(pk)
            serializer = self.serializer_class(audio)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        artist_fk = request.data.get('artist_fk')
        artist = Artist.objects.all().get(sequence=artist_fk)
        if(serializer.is_valid()):
            serializer.save(artist_fk=artist)
            return Response(serializer.data, status=status.HTTP_200_OK )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('sequence')
        try:
            audio = self.get_object(pk)
            audio.delete()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
#
# AudioLikeApi
#
# show all users likes specific audio
#
class AudioLikeApi(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer

    def get_object(self, pk):
        queryset = self.get_queryset()
        obj = queryset.get(sequence=pk)
        return obj

    def get(self, request, *args, **kwargs):
        audio_sequence = kwargs.get('sequence')
        try:
            audio = self.get_object(audio_sequence)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            userLike = UserLike.objects.filter(audio_fk=audio)
            serializer = UserLikeSerializer(userLike, many=True)
            return Response(serializer.data)
#
# ArtistFollowApi
#
# show all users follow specific artist
#
class ArtistFollowApi(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self, pk):
        queryset = self.get_queryset()
        obj = queryset.get(sequence=pk)
        return obj

    def get(self, request, *args, **kwargs):
        user_sequence = kwargs.get('sequence')
        try:
            user = self.get_object(user_sequence)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            userFollow = UserFollow.objects.filter(user_fk=user)
            serializer = UserFollowSerializer(userFollow, many=True)
            return Response(serializer.data)

class LikeApi(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = UserLike.objects.all()
    serializer_class = UserLikeSerializer
    def get_object(self, user, audio):
        queryset = self.get_queryset()
        obj = queryset.get(user_fk=user, audio_fk=audio)
        return obj
    def get(self, request, *args, **kwargs):
        user_sequence = request.query_params.get('user')
        audio_sequence = request.query_params.get('audio')
        all = request.query_params.get('all')
        if (all is not None and int(all) == 1):
            return Response(self.serializer_class(self.get_queryset(), many=True).data)
        else:
            try:
                user = User.objects.all().get(sequence=user_sequence)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            try:
                audio = Audio.objects.all().get(sequence=audio_sequence)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            try:
                relation = self.get_object(user,audio)
                serializer = UserLikeSerializer(relation)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
    def post(self, request, *args, **kwargs):
        user_sequence = request.data.get('user_fk')
        audio_sequence = request.data.get('audio_fk')
        try:
            user = User.objects.all().get(sequence=user_sequence)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            audio = Audio.objects.all().get(sequence=audio_sequence)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            relation = self.get_object(user, audio)
        except:
            serializer = UserLikeSerializer(data=request.data)
            if (serializer.is_valid()):
                serializer.save(audio_fk=audio, user_fk=user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        user_sequence = request.data.get('user_fk')
        audio_sequence = request.data.get('audio_fk')
        try:
            user = User.objects.all().get(sequence=user_sequence)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            audio = Audio.objects.all().get(sequence=audio_sequence)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            relation = self.get_object(user, audio)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            userLike = self.get_object(user,audio)
            userLike.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class FollowApi(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = UserFollow.objects.all()
    serializer_class = UserFollowSerializer
    def get_object(self, user, artist):
        queryset = self.get_queryset()
        obj = queryset.get(user_fk=user, artist_fk=artist)
        return obj
    def get(self, request, *args, **kwargs):
        artist_sequence = kwargs.get('sequence')
        all = request.query_params.get('all')
        if (all is not None and int(all) == 1):
            return Response(self.serializer_class(self.get_queryset(), many=True).data)
        else:
            try:
                artist = Artist.objects.all().get(sequence=artist_sequence)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            try:
                userLike = UserFollow.objects.filter(artist_fk = artist)
                serializer = UserFollowSerializer(userLike, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        user_sequence = request.data.get('user_fk')
        artist_sequence = request.data.get('artist_fk')
        try:
            user = User.objects.all().get(sequence=user_sequence)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            artist = Artist.objects.all().get(sequence=artist_sequence)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            relation = self.get_object(user, artist)
        except:
            serializer = UserFollowSerializer(data=request.data)
            if (serializer.is_valid()):
                serializer.save(artist_fk=artist, user_fk=user)
                serializer_list = UserFollowSerializer(UserFollow.objects.filter(artist_fk=artist),many=True)
                return Response(serializer_list, status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        user_sequence = request.data.get('user_fk')
        artist_sequence = request.data.get('artist_fk')
        try:
            user = User.objects.all().get(sequence=user_sequence)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            artist = Artist.objects.all().get(sequence=artist_sequence)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            relation = self.get_object(user, artist)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            userFollow = self.get_object(user,artist)
            userFollow.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)


#example http://api.soundcloud.com/tracks/27388810?client_id=
soundcloud_client_id = "&client_id=175c043157ffae2c6d5fed16c3d95a4c"
soundcloud_api_url = "http://api.soundcloud.com/tracks/"

class ChartApi(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    queryset = Chart.objects.all()
    serializer_class = ChartSerializer

    def get(self, request, *args, **kwargs):
        chart_type = int(kwargs.get('sequence'))
        target_set = None
        if chart_type==0:
            target_set = Beat.objects.all()
        elif chart_type == 1:
            target_set = Mixtape.objects.all()
        elif chart_type == 2:
            target_set = Artist.objects.all()
        rank_set = Ranking.objects.all()
        ranking_array = []
        for target in target_set:
            item = {}
            if chart_type == 0:
                item['score'] = UserLike.objects.filter(audio_fk=target.audio_info_fk).count()
            elif chart_type == 1:
                item['score'] = UserLike.objects.filter(audio_fk=target.audio_info_fk).count()
            elif chart_type == 2:
                item['score'] = UserFollow.objects.filter(artist_fk=target.sequence).count()
            item['target'] = target
            ranking_array.append(item)
        ranking_array.sort(key = lambda x: -x['score'])

        return Response(ranking_array,status=status.HTTP_200_OK)