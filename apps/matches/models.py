from django.db import models
from apps.general.models import DateBaseModel
from datetime import datetime

class Team(DateBaseModel):
    name = models.CharField(verbose_name="Team Name", max_length=255,)

    def __str__(self):
        return self.name


class Player(DateBaseModel):
    name = models.CharField(verbose_name="Player Name", max_length=255,)

    def __str__(self):
        return self.name


class Umpire(DateBaseModel):
    name = models.CharField(verbose_name="Umpire Name", max_length=255,)

    def __str__(self):
        return self.name


class Venue(DateBaseModel):
    name = models.CharField(verbose_name="Venue", max_length=255,)

    def __str__(self):
        return self.name

class Match(DateBaseModel):
    FIELD = 'field'
    BAT = 'bat'
    NORMAL = 'normal'
    TIE = 'tie'
    NORESULT = 'noresult'

    TOSS_DECISION = (
       (FIELD, 'Field'),
       (BAT, 'Bat'),
       )
    RESULT = (
       (NORMAL, 'Normal'),
       (TIE, 'Tie'),
       (NORESULT, 'NoResult'),
       )

    season = models.CharField(max_length=500, db_index=True)
    city = models.CharField(max_length=500, db_index=True)
    date = models.DateTimeField(default=datetime.now,db_index=True)
    team1 =  models.ForeignKey('Team',help_text="", related_name='match_team_1', on_delete=models.CASCADE, db_index=True)
    team2 =  models.ForeignKey('Team',help_text="", related_name='match_team_2', on_delete=models.CASCADE, db_index=True)
    toss_winner =  models.ForeignKey('Team',help_text="", related_name='toss_winner', on_delete=models.CASCADE, db_index=True)
    toss_decision = models.CharField(max_length=50, choices=TOSS_DECISION, default=BAT,)
    result = models.CharField(max_length=50, choices=RESULT, default=NORMAL,)
    dl_applied = models.CharField(max_length=500, db_index=True)
    winner =  models.ForeignKey('Team',help_text="", related_name='winner', on_delete=models.CASCADE, db_index=True)
    win_by_runs = models.CharField(max_length=500, db_index=True,  null=True, blank=True)
    win_by_wickets = models.CharField(max_length=500, db_index=True,  null=True, blank=True)
    player_of_match =  models.ForeignKey('Player',help_text="", related_name='match_player', on_delete=models.SET_NULL,null=True, blank=True, db_index=True)
    venue = models.ForeignKey('Venue',models.SET_NULL, related_name='match_venue',  null=True, blank=True, db_index=True)
    umpire1 =  models.ForeignKey('Umpire',models.SET_NULL, help_text="", related_name='umpire1',  null=True, blank=True, db_index=True)
    umpire2 =  models.ForeignKey('Umpire',models.SET_NULL, help_text="", related_name='umpire2', null=True, blank=True, db_index=True)
    umpire3 =  models.ForeignKey('Umpire',models.SET_NULL, help_text="", related_name='umpire3', null=True, blank=True, db_index=True)

 
class Deliveries(DateBaseModel):
    FIRST = '1'
    SECOND = '2'

    INNINGS = (
       (FIRST, '1'),
       (SECOND, '2'),
       )

    match =  models.ForeignKey('Match',help_text="", related_name='deliveries_match', on_delete=models.CASCADE, db_index=True)
    inning = models.CharField(max_length=50, choices=INNINGS, default=FIRST,)
    batting_team = models.ForeignKey('Team',help_text="", related_name="deliveries_bating_team", on_delete=models.CASCADE, db_index=True)
    bowling_team = models.ForeignKey('Team',help_text="", related_name='deliveries_bowling_team', on_delete=models.CASCADE, db_index=True)
    over = models.IntegerField(verbose_name="Over")
    ball = models.IntegerField(verbose_name="Ball")
    batsman = models.ForeignKey('Player',help_text="", related_name='deliveries_batsman', on_delete=models.CASCADE, db_index=True)
    non_striker = models.ForeignKey('Player',help_text="", related_name='deliveries_non_striker', on_delete=models.CASCADE, db_index=True)
    bowler = models.ForeignKey('Player',help_text="", related_name='deliveries_bowler', on_delete=models.CASCADE, db_index=True)
    is_super_over = models.BooleanField(default=False)
    wide_runs = models.IntegerField(verbose_name="Wide runs")
    bye_runs = models.IntegerField(verbose_name="Wide runs")
    legbye_runs = models.IntegerField(verbose_name="Wide runs")
    noball_runs = models.IntegerField(verbose_name="Wide runs")
    penalty_runs = models.IntegerField(verbose_name="Wide runs")
    batsman_runs = models.IntegerField(verbose_name="Wide runs")
    extra_runs = models.IntegerField(verbose_name="Wide runs")
    total_runs = models.IntegerField(verbose_name="Wide runs")
    player_dismissed = models.ForeignKey('Player',help_text="", related_name='deliveries_player_dismissed', on_delete=models.CASCADE, db_index=True)
    dismissal_kind = models.CharField(max_length=500, db_index=True)
    fielder = models.ForeignKey('Player',help_text="", related_name='deliveries_fielder', on_delete=models.CASCADE, db_index=True)
