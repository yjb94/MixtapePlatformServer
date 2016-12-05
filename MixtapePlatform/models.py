from __future__ import unicode_literals

from django.db import models

# Create your models here.
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
    artist_fk = models.ForeignKey(
        'Artist',
        on_delete = models.CASCADE,
    )
    stream_url = models.CharField(max_length=100)
    artwork_url = models.CharField(max_length=100)
    waveform_url = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

"""
sequence        Primary Key
user_info_fk    User Foreign Key
aka             Artist Nickname
"""
class Artist(models.Model):
    sequence = models.AutoField(primary_key=True)
    user_info_fk = models.ForeignKey(
        'User',
        on_delete = models.CASCADE,
    )
    aka = models.CharField(max_length=12)

"""
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