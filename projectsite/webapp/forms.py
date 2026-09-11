from django.forms import ModelForm 
from django import forms 
from .models import Task 
from .models import Note 
from .models import SubTask
from .models import Category


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

class CategoryForm(ModelForm):  
    class Meta: 
        model = Category  
        fields = "__all__" 