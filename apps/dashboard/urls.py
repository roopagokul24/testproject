from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.DashboardHomeView.as_view(), name='home'),
    path('upload-team', views.UploadTeamView.as_view(), name='upload-team'),
    path('upload-match', views.UploadMatchView.as_view(), name='upload-match'),
    path('upload-umpire', views.UploadUmpireView.as_view(), name='upload-umpire'),
    path('upload-venue', views.UploadVenueView.as_view(), name='upload-venue'),
    path('upload-player', views.UploadPlayerView.as_view(), name='upload-player'),
    path('teams', views.TeamView.as_view(), name='teams'),
    path('matches', views.MatchView.as_view(), name='matches'),
    path('umpires', views.UmpireView.as_view(), name='umpires'),
    path('venues', views.VenueView.as_view(), name='venues'),
    path('players', views.PlayerView.as_view(), name='players'),
    ]
