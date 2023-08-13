
from team.models import Team


def active_teams(request):
    if request.user.is_authenticated:
        if request.user.userprofile.active_team_id:
            teams = Team.objects.get(
                pk=request.user.userprofile.active_team_id)

            return {'active_team': teams}
    return {'active_team': None}
