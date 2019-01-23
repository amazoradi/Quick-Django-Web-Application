from django.urls import path
from . import views

# define a route for listing artists, and one for show a specific artist's details.
app_name = 'history'

urlpatterns = [
    path('', views.artists, name='artists'),
    path('<int:artist_id>/', views.details, name='details'),
    path('new_artist/', views.new_artist, name="new_artist"),
    path('<int:artist_id>/new_song/', views.new_song, name="new_song")
] 