
from django.urls import path

from project.views import projects, project, edit_project, task, edit_task

app_name = 'project'


urlpatterns = [
    path('', projects, name="projects"),
    path('<int:project_id>/', project, name="project"),
    path('edit/<int:project_id>/', edit_project, name="edit_project"),
    path('<int:project_id>/<int:task_id>/', task, name="task"),
    path('edit/<int:project_id>/<int:task_id>/', edit_task, name="edit_task"),
]
