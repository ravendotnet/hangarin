from django.forms import ModelForm 
from django import forms 
from .models import Task 
from .models import Note 
from .models import SubTask


class TaskForm(ModelForm):  
    class Meta: 
        model = Task  
        fields = "__all__" 

class NoteForm(ModelForm):  
    class Meta: 
        model = Note  
        fields = "__all__" 

class SubtaskForm(ModelForm):  
    class Meta: 
        model = SubTask  
        fields = "__all__" 