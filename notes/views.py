from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import *


def projects(request):
    projects_list = get_list_or_404(Project.objects.order_by('-date_update'))
    context = {
        'projects_list': projects_list,
    }
    return render(request, 'notes/projects.html', context)


def tasks(request, project_name):
    # tasks_list = Task.objects.order_by('-date_update')
    # project_id = get_object_or_404(Project.objects.get(name=project_name))
    project_id = get_object_or_404(Project, name=project_name)
    tasks_list = get_list_or_404(Task.objects.filter(project=project_id).order_by('-date_update'))
    context = {
        'tasks_list': tasks_list,
    }
    return render(request, 'notes/tasks.html', context)


def notes(request, project_name, task_name):
    # notes_list = Note.objects.order_by('-date_update')
    # task_id = get_object_or_404(Task.objects.get(name=task_name))
    task_id = get_object_or_404(Task, name=task_name)
    notes_list = get_list_or_404(Note.objects.filter(task=task_id).order_by('-date_update'))
    context = {
        'notes_list': notes_list,
    }
    return render(request, 'notes/notes.html', context)