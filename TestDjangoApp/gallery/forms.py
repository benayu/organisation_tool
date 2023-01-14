from django import forms
from .models import Photo


class PhotoForm(forms.ModelForm):
    name = forms.CharField(label='',widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Title'}))
    photo = forms.ImageField()
    favorite = forms.BooleanField(required=False, initial=None,label='Mark as Favorite',widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
    class Meta:
        model = Photo
        fields = ['name', 'photo', 'favorite']