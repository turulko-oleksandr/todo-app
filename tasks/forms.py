from django import forms
from .models import Task, Tag

from django.forms.widgets import TextInput, DateInput, CheckboxSelectMultiple


class TaskForm(forms.ModelForm):
    deadline = forms.DateField(
        widget=DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        required=False,
    )

    class Meta:
        model = Task
        fields = ['content', 'deadline', 'tags']
        widgets = {
            'content': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your task content'
            }),
            'tags': CheckboxSelectMultiple(attrs={
                'class': 'form-check-input',
            }),
        }


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter tag name (e.g., Work, Home)'
            }),
        }
