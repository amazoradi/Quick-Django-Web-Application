from django.db import models


class Artist(models.Model):
  artist_name = models.CharField(max_length=100)
  date_formed = models.IntegerField('date formed')


class Song(models.Model):
  song_name = models.CharField(max_length=200)
  album_name = models.CharField(max_length=200)

class Song_Artist(models.Model):
  song =  models.ForeignKey(Song, on_delete=models.CASCADE)
  artist = models.ForeignKey(Artist, on_delete=models.CASCADE)