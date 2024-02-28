from django import forms
from django.forms import inlineformset_factory
from .models import Garment, Operation

class OperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = ['operation_name', 'time_allowed']

OperationFormSet = inlineformset_factory(Garment, Operation, form=OperationForm, extra=20, can_delete=True)

class StartProductionForm(forms.Form):
    garment = forms.ModelChoiceField(queryset=Garment.objects.all())
    quantity = forms.IntegerField()
    operation = forms.ModelChoiceField(queryset=Operation.objects.none(), required=False)

    def __init__(self, *args, **kwargs):
        instance = kwargs.get('instance')
        if instance:
            initial = kwargs.get('initial', {})
            selected_garment = instance.garment
            initial['operation'] = selected_garment.operation_set.first()
            kwargs['initial'] = initial

        super().__init__(*args, **kwargs)

        if 'garment' in self.data:
            try:
                selected_garment_id = int(self.data.get('garment'))
                selected_garment = Garment.objects.get(id=selected_garment_id)
                self.fields['operation'].queryset = selected_garment.operation_set.all()
            except (ValueError, Garment.DoesNotExist):
                pass
        elif instance and instance.garment:
            self.fields['operation'].queryset = instance.garment.operation_set.all()
