from django.forms import ModelForm 
from django import forms 
from .models import Task 
from .models import Note 


class TaskForm(ModelForm):  
    class Meta: 
        model = Task  
        fields = "__all__" 

class NoteForm(ModelForm):  
    class Meta: 
        model = Note  
        fields = "__all__" 