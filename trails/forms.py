from django import forms
from .models import Comment

class CreateCommentForm(forms.ModelForm):
    description =  forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder': 'Your comment...:'}))
    class Meta:
        model = Comment
        fields=['comment']
        
