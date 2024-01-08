from django import forms
from django.forms import formset_factory
from .models import Operation

class OperationsForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = ['operation_name', 'time_allowed']

OperationFormSet = formset_factory(OperationsForm, extra=3) 
