"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import HomePageView
from webapp.views import TaskList, TaskCreateView, TaskUpdateView, TaskDeleteView
from webapp.views import NoteList, NoteCreateView, NoteUpdateView, NoteDeleteView
from webapp.views import SubtaskList, SubtaskCreateView, SubtaskUpdateView, SubtaskDeleteView
from webapp.views import CategoryList, CategoryCreateView, CategoryUpdateView, CategoryDeleteView
from webapp.views import PriorityList, PriorityCreateView, PriorityUpdateView, PriorityDeleteView
from webapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),

    path('task_list', TaskList.as_view(), name='task-list'),
    path('task_list/add', TaskCreateView.as_view(), name='task-add'),
    path('task_list/<pk>',TaskUpdateView.as_view(), name='task-update'),
    path('task_list/<pk>/delete', TaskDeleteView.as_view(), name='task-delete'), 

    path('note_list', NoteList.as_view(), name='note-list'), 
    path('note_list/add', NoteCreateView.as_view(), name='note-add'),
    path('note_list/<pk>',NoteUpdateView.as_view(), name='note-update'),
    path('note_list/<pk>/delete', NoteDeleteView.as_view(), name='note-delete'), 

    path('subtask_list', SubtaskList.as_view(), name='subtask-list'),
    path('subtask_list/add', SubtaskCreateView.as_view(), name='subtask-add'),
    path('subtask_list/<pk>',SubtaskUpdateView.as_view(), name='subtask-update'),
    path('subtask_list/<pk>/delete', SubtaskDeleteView.as_view(), name='subtask-delete'), 

    path('category_list', CategoryList.as_view(), name='category-list'),
    path('category_list/add', CategoryCreateView.as_view(), name='category-add'),
    path('category_list/<pk>',CategoryUpdateView.as_view(), name='category-update'),
    path('category_list/<pk>/delete', CategoryDeleteView.as_view(), name='category-delete'), 

    path('priority_list', PriorityList.as_view(), name='priority-list'),
    path('priority_list/add', PriorityCreateView.as_view(), name='priority-add'),
    path('priority_list/<pk>', PriorityUpdateView.as_view(), name='priority-update'),
    path('priority_list/<pk>/delete', PriorityDeleteView.as_view(), name='priority-delete'), 
]
