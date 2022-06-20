from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def projects(request):
    projects_list = Project.objects.order_by('-date_update')
    context = {
        'projects_list': projects_list,
    }
    return render(request, 'notes/projects.html', context)


def tasks(request, project_name):
    # tasks_list = Task.objects.order_by('-date_update')
    project_id = Project.objects.get(name=project_name)
    tasks_list = Task.objects.filter(project=project_id)
    context = {
        'tasks_list': tasks_list,
    }
    return render(request, 'notes/tasks.html', context)


def notes(request, project_name, task_name):
    # notes_list = Note.objects.order_by('-date_update')
    task_id = Task.objects.get(name=task_name)
    notes_list = Note.objects.filter(task=task_id)
    context = {
        'notes_list': notes_list,
    }
    return render(request, 'notes/notes.html', context)