from django.shortcuts import render
from django.http import HttpResponse
from .models import Artist
from .models import Song
from .models import Song_Artist
from django.template import loader
from django.shortcuts import get_object_or_404
# Create your views here.


# def index(request):
#   artist_list = Artist.objects.all()
#   context = {'artist_list': artist_list}
#   return render(request, 'history/index.html', context)
  # return HttpResponse("Hello, world. You're at the history index.")

def artists(request):
  artist_list = Artist.objects.all()
  context = {'artist_list': artist_list}
  return render(request, 'history/index.html', context)

def details(request, artist_id):
  # return HttpResponse(f"Hello, world. You're at the artist {artist_id} detail page.") 
  song_artist_list = get_object_or_404(Artist, id=artist_id)
  # song_list = (Artist, song_artist_list.artist_id)
  artist_songs = Song_Artist.objects.filter(artist_id = artist_id)
  song_list = [Song.objects.filter(id=song.song_id) for song in artist_songs]
  context = {'song_artist_list': song_artist_list,
              'song_list': song_list}  
  print(context)
  print("songlist:", song_list[0])
  return render(request, 'history/details.html', context)

