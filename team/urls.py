
from django.urls import path

from team.views import add_team, team, edit, activate_team

app_name = 'team'

urlpatterns = [
    path('add/', add_team, name="add"),
    path('edit/', edit, name="edit"),
    path('<int:team_id>/', team, name="team"),
    path('activate/<int:team_id>/', activate_team, name="activate_team"),
]
