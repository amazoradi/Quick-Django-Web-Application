from django.shortcuts import render
from django.http import HttpResponse
from .models import Artist
from .models import Song
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
  song_list = get_object_or_404(Artist, pk=artist_id)
  context = {'song_list': song_list}
  return render(request, 'history/details.html', context)

