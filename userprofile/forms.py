from django import forms
from Blog.models import Profile


class ProfileImage(forms.ModelForm):
    profile_img = forms.ImageField(
        label='Add Cover Image',
        widget=forms.ClearableFileInput(
            attrs={'class':'form-control','name':'image','type':'file','id':'formFile'}))
    class Meta:
        model = Profile
        fields  = ['profile_img']