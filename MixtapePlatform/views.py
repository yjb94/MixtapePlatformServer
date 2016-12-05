from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework import serializers, mixins
from rest_framework.generics import GenericAPIView

from MixtapePlatform.models import User
# Create your views here.

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

class UserApi(GenericAPIView, mixins.ListModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

def login_validate(request):
    