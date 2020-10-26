from django import forms

from .models import Post

class PostForm(forms.Form):
    text = forms.CharField(max_length=1000, widget=forms.Textarea)