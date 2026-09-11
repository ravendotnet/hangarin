from django.shortcuts import render

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from webapp.models import Task 
from webapp.models import Note
from webapp.models import SubTask
from webapp.forms import NoteForm
from webapp.forms import TaskForm
from webapp.forms import SubtaskForm
from django.urls import reverse_lazy  

 
class HomePageView(ListView): 
    model = Task 
    context_object_name = 'home' 
    template_name = "home.html" 

# Task
class TaskList(ListView): 
    model = Task
    context_object_name = 'task' 
    template_name = 'task_list.html' 
    paginate_by = 5 

class TaskCreateView(CreateView): 
    model = Task 
    form_class = TaskForm 
    template_name = 'task_form.html' 
    success_url = reverse_lazy('task-list')

class TaskUpdateView(UpdateView): 
    model = Task 
    form_class = TaskForm 
    template_name = 'task_form.html' 
    success_url = reverse_lazy('task-list') 

class TaskDeleteView(DeleteView): 
    model = Task
    template_name = 'task_del.html' 
    success_url = reverse_lazy('task-list') 

# Note
class NoteList(ListView): 
    model = Note
    context_object_name = 'note' 
    template_name = 'note_list.html' 
    paginate_by = 5 

class NoteCreateView(CreateView): 
    model = Note 
    form_class = NoteForm 
    template_name = 'note_form.html' 
    success_url = reverse_lazy('note-list')

class NoteUpdateView(UpdateView): 
    model = Note 
    form_class = NoteForm 
    template_name = 'note_form.html' 
    success_url = reverse_lazy('note-list') 

class NoteDeleteView(DeleteView): 
    model = Note
    template_name = 'note_del.html' 
    success_url = reverse_lazy('note-list') 

# SubTask
class SubtaskList(ListView): 
    model = SubTask
    context_object_name = 'subtask' 
    template_name = 'subtask_list.html' 
    paginate_by = 5 

class SubtaskCreateView(CreateView): 
    model = SubTask 
    form_class = SubtaskForm
    template_name = 'subtask_form.html' 
    success_url = reverse_lazy('subtask-list')

class SubtaskUpdateView(UpdateView): 
    model = SubTask 
    form_class = SubtaskForm
    template_name = 'subtask_form.html' 
    success_url = reverse_lazy('subtask-list') 

class SubtaskDeleteView(DeleteView): 
    model = SubTask
    template_name = 'subtask_del.html' 
    success_url = reverse_lazy('subtask-list') 