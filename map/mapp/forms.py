from django import forms
from .models import *

class TaskForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = []  # Поля, которые будут в форме