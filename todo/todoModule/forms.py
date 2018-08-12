from django import forms
from .models import TodoList
# from django.contrib.admin import widgets


class TodoForm(forms.ModelForm):
    title = forms.CharField(label='Title', max_length=100)
    content = forms.CharField(label='Description', required=False)
    # due_date = forms.DateTimeField(label='Due Date')
    due_date = forms.DateTimeField(widget=forms.TextInput(
                                attrs={
                                    'class':'datetimepicker',
                                }))
    # due_date = forms.SplitDateTimeField(widget=widgets.AdminSplitDateTime)

    class Meta:
        model = TodoList
        fields = ('title','content','due_date',)
        # widgets = {
        #     'due_date': forms.DateTimeInput(attrs={'id': 'datetimepicker12', 'class': 'datetime-input'})
        # }
        # widgets = {'due_date': forms.DateTimeInput(attrs={'class': 'datetime-input'})}


        # widgets = {'event_date': forms.DateInput(attrs={'class': 'datepicker'})}
        # exclude =['owner','active']

    def clean_date(self):
        datetime = self.cleaned_data['datetime']
        if datetime < datetime.datetime.now():
            raise forms.ValidationError("The time cannot be in the past!")
        return date

# class RegistrationForm(forms.ModelForm):
#     status = "completed"
#
#     class Meta:
#         model = TodoList
