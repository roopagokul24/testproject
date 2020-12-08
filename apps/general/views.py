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


from apps.matches.models import Match, Team, Player


# Create your views here.
class HomeView(TemplateView):
    template_name = 'general/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        matches = Match.objects.all()
        players = Player.objects.all()
        winner_dict = {}
        toss_winner_dict = {}
        player_of_match_dict = {}
        winner_dict_sorted = {}
        toss_winner_sorted = {}
        player_of_match_dict_sorted = {}

        teams = Team.objects.all()
        for team in teams:
            winner_dict[team] = matches.filter(winner=team).count()
        winner_dict_sorted = dict(sorted(winner_dict.items(), key=lambda item: -item[1]))
        context['winner_dict_sorted'] = list(winner_dict_sorted)[:4]


        for team in teams:
            toss_winner_dict[team] = matches.filter(toss_winner=team).count()
        toss_winner_sorted = dict(sorted(toss_winner_dict.items(), key=lambda item: -item[1]))
        context['winner_dict_sorted'] = list(winner_dict_sorted)[:1]

        for player in players:
            player_of_match_dict[player] = matches.filter(player_of_match=player).count()
        player_of_match_dict_sorted = dict(sorted(player_of_match_dict.items(), key=lambda item: -item[1]))
        context['player_of_match_dict_sorted'] = list(player_of_match_dict_sorted)[:1]

        return context
