from django.urls import path
from . import views


app_name = 'notes'
urlpatterns = [
    path('', views.projects, name='projects'),
    path('<str:project_name>/', views.tasks, name='tasks'),
    path('<str:project_name>/<str:task_name>/', views.notes , name='notes'),
]