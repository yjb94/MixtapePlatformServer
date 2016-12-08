from math import radians

from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import serializers, mixins
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from MixtapePlatform.models import User
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
        pk = request.query_params.__getitem__('sequence')
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        pk = request.query_params.__getitem__('sequence')
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



    def delete(self, request, *args, **kwargs):
        pk = request.query_params.__getitem__('sequence')
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LoginApi(GenericAPIView, mixins.ListModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get_object(self, email, password):
        queryset = self.get_queryset()
        obj = queryset.get(email=id, password=password)
        return obj

    def post(self, request, *args, **kwargs):
        print(1)
        email = request.data.get('email')
        password = request.data.get('password')
        user = self.get_object(email,password)
        if (user):
            return Response(user, status=status.HTTP_200_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
