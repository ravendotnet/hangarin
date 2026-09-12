from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.utils import timezone 

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from webapp.models import Task 
from webapp.models import Note
from webapp.models import SubTask
from webapp.models import Category
from webapp.models import Priority
from webapp.forms import PriorityForm
from webapp.forms import CategoryForm
from webapp.forms import NoteForm
from webapp.forms import TaskForm
from webapp.forms import SubtaskForm
from django.urls import reverse_lazy  

 
class HomePageView(LoginRequiredMixin, ListView): 
    model = Task 
    context_object_name = 'home' 
    template_name = "home.html" 

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs) 
        context["total_task"] = Task.objects.count() 
        context["total_notes"] = Note.objects.count() 
        context["total_subtask"] = SubTask.objects.count() 
         
        today = timezone.now().date() 
        context["task_deadline"] = Task.objects.filter(
            deadline=today
        ).count()

        return context    

# Task
class TaskList(ListView): 
    model = Task
    context_object_name = 'task' 
    template_name = 'task_list.html' 
    paginate_by = 5 
    ordering = ["title"]
    
    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.GET.get('q')

        if query:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query) |
                Q(category__name__icontains=query) |
                Q(priority__name__icontains=query)
            )

        return qs

    def get_ordering(self):
        allowed = [
            "title",
            "status",
            "category__name",
            "priority__name",
        ]

        sort_by = self.request.GET.get("sort_by")

        if sort_by in allowed:
            return [sort_by]

        return self.ordering

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

    ordering = ['content']

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.GET.get('q')

        if query:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(task__title__icontains=query)
            )

        return qs

    def get_ordering(self):
        allowed = [
            'content',
            'task__title',
        ]

        sort_by = self.request.GET.get('sort_by')

        if sort_by in allowed:
            return [sort_by]

        return self.ordering

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

    ordering = ['title']

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.GET.get('q')

        if query:
            qs = qs.filter(
                Q(title__icontains=query) |
                Q(status__icontains=query) |
                Q(parent_task__title__icontains=query)
            )

        return qs

    def get_ordering(self):
        allowed = [
            'title',
            'status',
            'parent_task__title',
        ]

        sort_by = self.request.GET.get('sort_by')

        if sort_by in allowed:
            return [sort_by]

        return self.ordering

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

# Categories
class CategoryList(ListView): 
    model = Category
    context_object_name = 'category' 
    template_name = 'category_list.html' 
    paginate_by = 5 

    ordering = ['name']

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.GET.get('q')

        if query:
            qs = qs.filter(
                Q(name__icontains=query) |
                Q(task__title__icontains=query)
            ).distinct()

        return qs

    def get_ordering(self):
        allowed = [
            'name',
        ]

        sort_by = self.request.GET.get('sort_by')

        if sort_by in allowed:
            return [sort_by]

        return self.ordering

class CategoryCreateView(CreateView): 
    model = Category 
    form_class = CategoryForm
    template_name = 'category_form.html' 
    success_url = reverse_lazy('category-list')

class CategoryUpdateView(UpdateView): 
    model = Category 
    form_class = CategoryForm
    template_name = 'category_form.html' 
    success_url = reverse_lazy('category-list') 

class CategoryDeleteView(DeleteView): 
    model = Category
    template_name = 'category_del.html' 
    success_url = reverse_lazy('category-list')

# Priority
class PriorityList(ListView): 
    model = Priority
    context_object_name = 'priority' 
    template_name = 'priority_list.html' 
    paginate_by = 5 

    ordering = ['name']

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.GET.get('q')

        if query:
            qs = qs.filter(
                Q(name__icontains=query)
            )

        return qs

    def get_ordering(self):
        allowed = [
            'name',
        ]

        sort_by = self.request.GET.get('sort_by')

        if sort_by in allowed:
            return [sort_by]

        return self.ordering

class PriorityCreateView(CreateView): 
    model = Priority 
    form_class = PriorityForm
    template_name = 'priority_form.html' 
    success_url = reverse_lazy('priority-list')

class PriorityUpdateView(UpdateView): 
    model = Priority 
    form_class = PriorityForm
    template_name = 'priority_form.html' 
    success_url = reverse_lazy('priority-list') 

class PriorityDeleteView(DeleteView): 
    model = Priority
    template_name = 'priority_del.html' 
    success_url = reverse_lazy('priority-list')