from django import forms
from django.forms import widgets

class TodoForm(forms.Form):
    text = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 
    'Enter todo e.g Delete junk files', 'aria-label': 'Todo', 'aria-describedby' : 'add-btn'}))
