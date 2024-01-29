from django import forms
from . models import *

class update_form(forms.ModelForm):
    
    class Meta:
        model = task
        fields = ['task_name','priority','date']