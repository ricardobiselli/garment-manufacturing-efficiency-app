from .models import Garment, Operation, OperationRecord
from django.shortcuts import render, redirect, get_object_or_404
from .models import Garment
from .forms import OperationFormSet
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt


def add_garment(request):
    if request.method == 'POST':
        garment_name = request.POST.get('name')
        if garment_name:
            garment = Garment.objects.create(name=garment_name)

            formset = OperationFormSet(request.POST, instance=garment)

            if formset.is_valid():
                formset.save()

                return redirect('add_garment_success')

    else:
        formset = OperationFormSet()

    return render(request, 'add_garment.html', {'formset': formset})


def home_view(request):
    return render(request, 'home.html')


def add_garment_success(request):
    return render(request, 'add_garment_success.html')


def select_garment(request):
    garments = Garment.objects.all()
    selected_garment = None
    selected_operation = None
    quantity = None

    if request.method == "POST":
        selected_garment_id = request.POST.get('garment')
        if selected_garment_id:
            selected_garment = Garment.objects.get(id=selected_garment_id)

            selected_operation_id = request.POST.get('operation')
            if selected_operation_id:
                selected_operation = Operation.objects.get(
                    id=selected_operation_id)
                quantity = request.POST.get('quantity')

    return render(request, 'select_garment.html', {'garments': garments, 'selected_garment': selected_garment, 'selected_operation': selected_operation, 'quantity': quantity})


def start_production(request):
    selected_garment_id = request.POST.get('garment')
    selected_operation_id = request.POST.get('operation')
    quantity = request.POST.get('quantity')

    selected_garment = Garment.objects.get(
        id=selected_garment_id) if selected_garment_id else None
    selected_operation = Operation.objects.get(
        id=selected_operation_id) if selected_operation_id else None

    context = {
        'selected_garment': selected_garment,
        'selected_operation': selected_operation,
        'quantity': quantity,
        'selected_garment_id': selected_garment_id,
    }

    

    return render(request, 'start_production.html', context)


def get_operations(request, garment_id):
    print(f"Received request for garment_id: {garment_id}")
    try:
        garment = Garment.objects.get(id=garment_id)
        operations = garment.operation_set.all()
        data = [{'id': operation.id, 'operation_name': operation.operation_name} for operation in operations]
        return JsonResponse(data, safe=False)
    except Garment.DoesNotExist:
        return JsonResponse([], safe=False)

@csrf_exempt
def update_operation(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Extract relevant data from the JSON
            total_elapsed = data.get('totalElapsed')
            individual_times = data.get('individualTimes')
            percentage_progress = data.get('percentageProgress')
            selected_garment_id = data.get('selectedGarmentId')
            print('Selected Garment ID:', selected_garment_id)

            # Assuming you have a Garment instance
            garment = Garment.objects.get(id=selected_garment_id)

            # Save the data to your OperationRecord model or any other relevant model
            operation_record = OperationRecord.objects.create(
                garment=garment,
                elapsed_time=total_elapsed,
                efficiency=0,  # You need to calculate efficiency based on your logic
                progress_percentage=percentage_progress
            )

            return JsonResponse({'status': 'success'})
        except json.JSONDecodeError as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)
