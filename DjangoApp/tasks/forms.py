from django import forms
from .models import Task
import datetime as dt

class DateInput(forms.DateInput):
    input_type = 'date'

class TaskForm(forms.ModelForm):
    summary = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "What is the task?", "class": "form-control"}))
    description = forms.CharField(required=False, label='', widget=forms.Textarea(attrs={"placeholder":"Additional information...","class": "form-control", "rows": 10, "cols": 120}))
    progress = forms.IntegerField(label='Progress (0-100)', initial=0, widget=forms.NumberInput(attrs={"class":"form-control" }))
    date_due = forms.DateField(label="Due date", initial=dt.date.today(), widget=forms.widgets.DateInput(attrs={"type": "date", "class":"form-control"}))
    time_due = forms.CharField(label="Time due", initial=dt.datetime.now().time().strftime('%H:%M'), widget=forms.widgets.TimeInput(attrs={"type":"time", "class":"form-control"}))

    class Meta:
        model = Task
        fields = [
            'summary',
            'description',
            'progress',
            'date_due',
            'time_due'
        ]

    def clean_progress(self, *args, **kwargs):
        progress = self.cleaned_data.get("progress")
        if progress > 100 or progress < 0:
            raise forms.ValidationError("Progress should be 0-100")
        return progress


