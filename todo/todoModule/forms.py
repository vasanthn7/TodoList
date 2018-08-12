from django import forms
from .models import TodoList

class TodoForm(forms.ModelForm):
    title = forms.CharField(label='Title', max_length=100)
    content = forms.CharField(label='Description', required=False)
    due_date = forms.DateTimeField(label='Due Date')


    class Meta:
        model = TodoList
        fields = ('title','content','due_date',)

        # widgets = {'event_date': forms.DateInput(attrs={'class': 'datepicker'})}
        # exclude =['owner','active']

    def clean_date(self):
        datetime = self.cleaned_data['datetime']
        if datetime < datetime.datetime.now():
            raise forms.ValidationError("The time cannot be in the past!")
        return date
