from django import forms
from .models import category, report

class CommentForm(forms.ModelForm):
    class Meta:
        model = report
        exclude = ['user','time_uploaded',]
