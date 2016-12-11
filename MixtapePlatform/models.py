from __future__ import unicode_literals

from rest_framework import serializers
from django.db import models

# Create your models here.
"""
class User

sequence        Primary Key
email           Email
password        Password
profile_url     Profile Image Url
thumbnail_url   Thumbnail Image Url
nickname        Nickname
"""
class User(models.Model):
    sequence = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    profile_url = models.CharField(max_length=100)
    thumbnail_url = models.CharField(max_length=100)
    nickname = models.CharField(max_length=12)

"""
class Artist

sequence        Primary Key
user_info_fk    User Foreign Key
aka             Artist Nickname
"""
class Artist(models.Model):
    sequence = models.AutoField(primary_key=True)
    user_info_fk = models.ForeignKey(User, related_name="artist_fk", on_delete=models.CASCADE)
    aka = models.CharField(max_length=12)
"""
class Audio

sequence        Primary Key
artist_fk       Artist Foreign Key
stream_url      Stream Mp3  Url
artwork_url     Artwork Image Url
waveform_url    Waveform Image Url
description     Description about Audio
"""
class Audio(models.Model):
    sequence = models.AutoField(primary_key=True)
    artist_fk = models.ForeignKey(Artist, related_name="Audio_fk", on_delete = models.CASCADE)
    stream_url = models.CharField(max_length=100)
    artwork_url = models.CharField(max_length=100)
    waveform_url = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
"""
class Beat

sequence
audio_info_fk
soundcloud_id
"""
class Beat(models.Model):
    sequence = models.AutoField(primary_key=True)
    audio_info_fk = models.ForeignKey(
        Audio,
        on_delete = models.CASCADE
    )
    sc_id = models.CharField(max_length=100)

"""
class Mixtape

sequence
original_beat_fk
audio_info_fk
voice_url
lyrics
"""
class Mixtape(models.Model):
    sequence = models.AutoField(primary_key=True)
    original_beat_fk = models.ForeignKey(
        Beat,
        on_delete = models.CASCADE
    )
    audio_info_fk = models.ForeignKey(
        Audio,
        on_delete = models.CASCADE
    )
    voice_url = models.CharField(max_length=100)
    lyrics = models.CharField(max_length=2048)


"""
class Chart

sequence        Primary Key
chart_type      Type of Chart ( Artist, Beat, Mixtape )
date            Date of Chart First Made
"""
class Chart(models.Model):
    sequence = models.AutoField(primary_key=True)
    chart_type = models.IntegerField()
    date = models.DateField(auto_now=False, auto_now_add=True)
"""
class Ranking

sequence        Primary Key
audio_fk        Audio Foreign Key
rank            Audio's Rank
"""
class Ranking(models.Model):
    sequence = models.AutoField(primary_key=True)
    audio_fk = models.ForeignKey(Audio, related_name="ranking_fk", on_delete=models.CASCADE)
    rank = models.IntegerField()
"""
class ChartRanking

sequence        Primary Key
chart_fk        Chart Foreign Key
ranking_fk      Ranking Foreign Key
"""
class ChartRanking(models.Model):
    sequence = models.AutoField(primary_key=True)
    chart_fk = models.ForeignKey(Chart, related_name="chartRanking_fk", on_delete=models.CASCADE)
    ranking_fk = models.ForeignKey(Ranking, related_name="chartRanking_fk", on_delete=models.CASCADE)

class UserLike(models.Model):
    sequence = models.AutoField(primary_key=True)
    user_fk = models.ForeignKey(User, related_name="userLike_fk", on_delete=models.CASCADE)
    audio_fk = models.ForeignKey(Audio, related_name="userLike_fk", on_delete=models.CASCADE)

class UserFollow(models.Model):
    sequence = models.AutoField(primary_key=True)
    user_fk = models.ForeignKey(User, related_name="userFollow_fk", on_delete=models.CASCADE)
    artist_fk = models.ForeignKey(Artist, related_name="userFollow_fk", on_delete=models.CASCADE)