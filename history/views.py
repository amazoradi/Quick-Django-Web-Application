from django.shortcuts import render
from .models import Artist
from .models import Song
from .models import Song_Artist
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def artists(request):
  artist_list = Artist.objects.all()
  context = {'artist_list': artist_list}
  return render(request, 'history/index.html', context)

def details(request, artist_id):
  song_artist_list = get_object_or_404(Artist, id=artist_id)
  artist_songs = Song_Artist.objects.filter(artist_id = artist_id)
  song_list = [Song.objects.filter(id=song.song_id) for song in artist_songs]
  context = {'song_artist_list': song_artist_list,
              'song_list': song_list}  
  return render(request, 'history/details.html', context)

# def new_song(request):
#   new_song_name = request.POST["song_name"]
#   new_song_album = request.POST["song_album"]
#   artist = request.POST["artist"]
#   a = Artist.object.get(name=artist)
#   Song.objects.create({"name": new_song_name, "new_song_album": new_song_album, "artist": a})
 

# def new_song(request, artist_id):
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question': question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing
#         # with POST data. This prevents data from being posted twice if a
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def new_artist(request):
  artist = request.POST['artist_name']
  date = request.POST['date_formed']
  new_artist = Artist(artist_name=artist, date_formed=date)
  new_artist.save()
  return HttpResponseRedirect(reverse('history:details', args=(new_artist.id,)))

def new_song(request, artist_id):
  song = request.POST['song_name']
  album = request.POST['album_name']
  new_song = Song(song_name=song, album_name=album)
  new_song.save()
  new_song_artist = Song_Artist(artist_id=artist_id, song_id=new_song.id)
  new_song_artist.save()
  return HttpResponseRedirect(reverse('history:artists'))