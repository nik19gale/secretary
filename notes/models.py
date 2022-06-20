from django.db import models
from django.utils import timezone


class Project(models.Model):
    name = models.CharField(max_length=100)
    date_create = models.DateTimeField(default=timezone.now)
    date_update = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=50, null=True, blank=True)
    date_create = models.DateTimeField(default=timezone.now)
    date_update = models.DateTimeField(default=timezone.now)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Note(models.Model):
    date_create = models.DateTimeField(default=timezone.now)
    date_update = models.DateTimeField(default=timezone.now)
    text = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)


    def __str__(self):
        return self.text