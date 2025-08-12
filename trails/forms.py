from django import forms
from .models import Trail

difficulty_level=[
    ("easy","EASY"),
    ("moderate","MODERATE"),
    ("challenging","CHALLEGNING"),
    ("hard","HARD"),
]
type_trail=[
    ("hiking","HIKING"),
    ("bike","Bike"),
    ("running","RUNNING"),
]
class CreateTrailForm(forms.ModelForm):
    description =  forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder': 'Trail description:'}))
    difficulty_level=forms.ChoiceField(choices=difficulty_level,widget=forms.Select(
        attrs={'class': 'form-control','placeholder': 'Trail difficulty:'}))
    type_trail=forms.ChoiceField(choices=type_trail,widget=forms.Select(
        attrs={'class': 'form-control','placeholder': 'Type:'}))
    duration=forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder': 'Trail duration:'}))
    distance=forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder': 'Distance:'}))
    meeting_point=forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control','placeholder': 'Meeting location:'}))
    date=forms.DateTimeField()
    class Meta:
        model = Trail
        fields=['description','coordinator','difficulty_level',
                'type','duration','meeting_point','date']
        
