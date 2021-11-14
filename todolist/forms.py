from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TimeInput(attrs={'placeholder':'Add new task....'}))

    class Meta:
        model = Task
        fields = '__all__'
