from django import forms
from .models import *
import random as rnd


class StreetsForm(forms.ModelForm):
    class Meta:
        model = Streets
        fields = ['']  # Поля, которые будут в форме