from django import forms
from .models import Person

class ContactForm(forms.ModelForm):
    title = forms.CharField(required=False, label="Title", widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label="First Name", widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(required=False, label="Last Name", widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=False, label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.CharField(required=False, label="Phone", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    description = forms.CharField(required=False, label="Description", widget=forms.Textarea(attrs={'class':'form-control'}))
    department = forms.CharField(required=False, label="Department", widget=forms.TextInput(attrs={'class': 'form-control'}))
    favorite = forms.BooleanField(required=False, label="Mark as Favorite", widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
    class Meta:
        model = Person
        fields = [
            'title',
            'first_name',
            'last_name',
            'email',
            'phone',
            'description',
            'department',
            'favorite',
            # 'picture'
        ]