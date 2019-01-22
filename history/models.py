from django.db import models


class Artist(models.Model):
  artist_name = models.CharField(max_length=100)
  date_formed = models.IntegerField('date formed')


class Song(models.Model):
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
  song_name = models.CharField(max_length=200)
  album_name = models.CharField(max_length=200)