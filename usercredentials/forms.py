from django.contrib.auth.forms import UserCreationForm
from .models import Profile
from django import forms

class ProfileCreationForm(UserCreationForm):
    address = forms.CharField(widget=forms.Textarea(attrs={'rows':3, 'placeholder':'line1\ncity\nstate'}))
    class  Meta:
        model = Profile
        fields = ['username', 'email', 'firstName', 'lastName', 'address', 'profilePicture']