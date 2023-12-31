
from django.contrib.auth.models import User
from django.db import models

from team.models import Team

# Create your models here.


class Project(models.Model):
    team = models.ForeignKey(
        Team, related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    created_by = models.ForeignKey(
        User, related_name='projects', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return str(self.title)

    def registered_time(self):
        return 0

    def num_tasks_todo(self):
        return 0


class Task(models.Model):

    TODO = 'todo'
    DONE = 'done'
    ARCHIVED = 'archived'

    CHOICES_STATUS = (
        (TODO, 'Todo'),
        (DONE, 'Done'),
        (ARCHIVED, 'Archived')
    )

    team = models.ForeignKey(Team, related_name='tasks',
                             on_delete=models.CASCADE)
    project = models.ForeignKey(
        Project, related_name='tasks', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    created_by = models.ForeignKey(
        User, related_name='tasks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, choices=CHOICES_STATUS, default=TODO)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def registered_time(self):
        return 0
