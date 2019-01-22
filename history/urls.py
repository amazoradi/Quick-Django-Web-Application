from django.urls import path
from . import views

# define a route for listing artists, and one for show a specific artist's details.
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.artists, name='artists'),
    path('<int:artist_id>', views.details, name='details'),
] 