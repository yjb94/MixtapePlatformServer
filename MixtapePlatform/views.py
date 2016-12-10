from math import radians

from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import serializers, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from MixtapePlatform.models import User, Audio, Mixtape, Beat
from MixtapePlatform.serializers import UserSerializer
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
        if(all is not None):
            return self.list(request,*args,**kwargs)
        else:
            try:
                user = self.get_object(pk)
                serializer = UserSerializer(user, data=request.data)
                if (serializer.is_valid()):
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)



    def post(self, request, *args, **kwargs):
        request.data.profile_url = "http://placehold.it/300X300"
        request.data.thumbnail_url = "http://placehold.it/1600X900"
        serializer = UserSerializer(data=request.data)
        aka = request.data.get('aka')
        if(serializer.is_valid()):
            serializer.save()
            #serializer2
            return Response(serializer.data, status=status.HTTP_201_CREATED )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        pk = request.query_params.get('sequence')
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        pk = request.query_params.get('sequence')
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LoginApi(GenericAPIView, mixins.ListModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_object(self, email, password):
        queryset = self.get_queryset()
        obj = queryset.get(email=email, password=password)
        return obj

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = self.get_object(email,password)

        serializer = UserSerializer(user)

        if (user):
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

#example http://api.soundcloud.com/tracks/27388810?client_id=
soundcloud_client_id = "?client_id=175c043157ffae2c6d5fed16c3d95a4c"
soundcloud_api_url = "http://api.soundcloud.com/    tracks/"

#class AudioAPI(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
#    queryset = Audio.objects.all()
#    serializer_class = AudioSerializer
