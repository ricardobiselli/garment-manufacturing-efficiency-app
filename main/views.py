from django.forms import formset_factory
from django.shortcuts import render, redirect
from .models import Garment, Operation
from .forms import OperationFormSet

from django.shortcuts import render, redirect
from .forms import OperationFormSet

def add_garment(request):
    if request.method == 'POST':
        formset = OperationFormSet(request.POST)
        if formset.is_valid():
            garment_name = request.POST.get('garment_name')
            garment = Garment.objects.create(name=garment_name)
            
            for form in formset:
                if form.is_valid():
                    operation_name = form.cleaned_data.get('operation_name')
                    time_allowed = form.cleaned_data.get('time_allowed')
                    Operation.objects.create(
                        garment_name=garment,
                        operation_name=operation_name,
                        time_allowed=time_allowed
                    )
            
            return redirect('add_garment_success')  
    else:
        formset = OperationFormSet()

    return render(request, 'add_garment.html', {'formset': formset})


"""OperationFormSet = formset_factory(OperationsForm, extra=1)
    
    if request.method == 'POST':
        formset = OperationFormSet(request.POST)
        garment_name = request.POST.get('garment_name')
        
        print("Formset is valid:", formset.is_valid())
        print("Formset errors:", formset.errors)
        
        if garment_name and formset.is_valid():
            print("Formset cleaned data:", formset.cleaned_data)
            print(f"Garment Name: '{garment_name}'")

            garment = Garment.objects.create(name=garment_name)
            print(f"Garment '{garment_name}' created")

            for i, form in enumerate(formset):
                print(f"Iteration {i+1} in the for loop")
                
                operation_name = form.cleaned_data.get('operation_name')
                time_allowed = form.cleaned_data.get('time_allowed')
                
                if operation_name and time_allowed:
                    new_operation = Operation.objects.create(
                        garment_name=garment,
                        operation_name=operation_name,
                        time_allowed=time_allowed
                    )
                    print(f"Operation {i+1} - Name: '{operation_name}', Time Allowed: {time_allowed}")
                    print(f"Associated with Garment '{garment_name}'")

            return redirect('add_garment_success')
        else:
            print("Form is not valid or garment name is missing")

    else:
        formset = OperationFormSet()

    return render(request, 'add_garment.html', {'formset': formset})"""




def select_garment(request):
    garments = Garment.objects.all()
    return render(request, 'select_garment.html', {'garments': garments})

def home_view(request):
    return render(request, 'home.html')

def start_production(request):
    return render(request, 'start_production.html')
    
def add_garment_success(request):
    return render(request, 'add_garment_success.html')