from django.contrib import admin
from apps.matches.models import Team, Player, Umpire, Venue, Match, Deliveries

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Umpire)
admin.site.register(Venue)
admin.site.register(Match)
admin.site.register(Deliveries)
