from .models import Note
from django import forms
from ckeditor_uploader.fields import RichTextUploadingFormField, RichTextUploadingField
from ckeditor.fields import RichTextFormField
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from .models import Note


class NoteForm(forms.ModelForm):
    title = forms.CharField(initial="Untitled",label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Untitled'}))
    content = RichTextFormField(label='',widget=CKEditorWidget())
    favorite = forms.BooleanField(required=False, label='Mark as Favorite',widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))

    class Meta:
        model = Note
        fields = [
            'title',
            'content',
            'favorite'
        ]

