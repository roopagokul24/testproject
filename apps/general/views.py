import datetime
import openpyxl
from django.db.models import Avg, Max, Min
from django.db.models import Count,Func, F, Value
from django.db.models.functions import Sqrt
from django.utils import timezone
from django.conf import settings
# from dateutil import parser


from django.db.models import Q
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic import TemplateView,View, CreateView
from django.views.generic.edit import FormView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin


from apps.matches.models import Match, Team, Player, Venue


# Create your views here.
class HomeView(TemplateView):
    template_name = 'general/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        season = self.request.COOKIES.get('season')
        matches = Match.objects.all()
        players = Player.objects.all()
        venues = Venue.objects.all()
        winner_dict = {}
        most_matches = {}
        toss_winner_dict = {}
        player_of_match_dict = {}
        most_wins_top_team = {}
        winner_dict_sorted = {}
        toss_winner_sorted = {}
        player_of_match_dict_sorted = {}
        most_wins_top_team_sorted = {}


        teams = Team.objects.all()
        for team in teams:
            winner_dict[team] = matches.filter(Q(winner=team) & Q(season=season)).count()
        winner_dict_sorted = dict(sorted(winner_dict.items(), key=lambda item: -item[1]))
        context['winner_dict_sorted'] = list(winner_dict_sorted)[:4]
        winner = list(winner_dict_sorted)[:1]

        matches_per_season = Match.objects.filter(season=season)
        win_by_runs__maximum = matches_per_season.aggregate(Max('win_by_runs'))['win_by_runs__max']
        context['run_margin_highest_match'] =  matches_per_season.filter(win_by_runs=win_by_runs__maximum).distinct('winner')

        for team in teams:
            toss_winner_dict[team] = matches.filter(Q(toss_winner=team) & Q(season=season)).count()
        toss_winner_sorted = dict(sorted(toss_winner_dict.items(), key=lambda item: -item[1]))
        context['toss_winner_sorted'] = list(toss_winner_sorted)[:1]

        for player in players:
            player_of_match_dict[player] = matches.filter(Q(player_of_match=player) & Q(season=season)).count()
        player_of_match_dict_sorted = dict(sorted(player_of_match_dict.items(), key=lambda item: -item[1]))
        context['player_of_match_dict_sorted'] = list(player_of_match_dict_sorted)[:1]


        toss_decision = matches.filter(Q(toss_decision=Match.BAT) & Q(season=season)).count()
        total = matches.filter(season=season).count()
        percentage = toss_decision*100/total

        for venue in venues:
            most_wins_top_team[venue]= matches.filter(Q(winner=winner[0]) & Q(venue=venue) & Q(season=season)).count()
            most_matches[venue] = matches.filter(Q(venue=venue) & Q(season=season)).count()

        most_matches_sorted = dict(sorted(most_matches.items(), key=lambda item: -item[1]))
        most_wins_top_team_sorted = dict(sorted(most_wins_top_team.items(), key=lambda item: -item[1]))


        context['most_matches'] =  list(most_matches_sorted)[:1]
        context['most_wins_top_team'] =  list(most_wins_top_team_sorted)[:1]
        context['percentage'] = percentage
        context['winner'] = winner

        return context
