from django import forms
from .models import Event


class Event_Entry(forms.ModelForm):
    title = forms.CharField(label="", widget=forms.Textarea(attrs={"rows":1, "placeholder":"Give a catchy title!", }))
    body = forms.CharField(label="", widget=forms.Textarea(attrs={"rows": 4, "placeholder": "Enter about your event!", }))
    flat_no = forms.CharField(label="", widget=forms.Textarea(attrs={"rows":1, "placeholder":"Enter the location!", }))

    class Meta:
        model = Event
        fields = ["title","body","flat_no"]