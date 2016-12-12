"""MixtapePlatformServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view

from MixtapePlatform.views import *

schema_view = get_swagger_view(title='Snippets API')

urlpatterns = [
    url('^$', schema_view),
    url(r'^admin/', admin.site.urls),
    url(r'^api/user/$', UserApi.as_view()),
    url(r'^api/login', LoginApi.as_view()),
    url(r'^api/audio/(?P<sequence>[0-9]+)$', AudioDetailApi.as_view()),
    url(r'^api/audio/like/(?P<sequence>[0-9]+)/$', AudioLikeApi.as_view()),
    url(r'^api/audio/$', AudioApi.as_view()),
    url(r'^api/artist/follow/(?P<sequence>[0-9]+)/$', ArtistFollowApi.as_view()),
    url(r'^api/artist/(?P<sequence>[0-9]+)/$', ArtistDetailApi.as_view()),
    url(r'^api/artist/$', ArtistApi.as_view()),
    url(r'^api/like', LikeApi.as_view()),
    url(r'^api/follow', FollowApi.as_view()),
    url(r'^api/chart/(?P<sequence>[0-2]+)/$', ChartApi.as_view()),
    url(r'^api/beat/$', BeatApi.as_view()),
    url(r'^api/mixtape/$', MixtapeApi.as_view()),
    #url(r'^api/artist/mixtape/(?P<sequence>[0-9]+)/$', ArtistMixtapeApi.as_view()),
    #url(r'^api/artist/follower/(?P<sequence>[0-9]+)/$', ArtistFollowerApi.as_view()),
]

