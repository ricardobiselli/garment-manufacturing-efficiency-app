import time
from  models import Garment

garments_list = []

#############################################################
#stop watch
def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    return f"time elapsed = {hours}:{mins}:{sec:.2f}"


def measure_time():
    input("Press ENTER to start")
    start_time = time.time()

    input("Press ENTER to STOP")
    end_time = time.time()

    time_elapsed = end_time - start_time
    return time_elapsed

#elapsed_time = measure_time()
#print(time_convert(elapsed_time))

#############################################################


def main_app():
    while True:
        print("Enter the name of the garment (or 'done' to finish adding garments):")
        garment_name = input()
        if garment_name.lower() == 'done':
            break
        garment = Garment(garment_name)

        while True:
            print(f"Enter an operation for {garment_name} (or 'done' to finish adding operations for this garment):")
            operation = input()
            if operation.lower() == 'done':
                break
            print(f"Enter estimated time (in minutes) allowed for operation '{operation}':")
            time_allowed = float(input())  

            garment.append_operations(operation, time_allowed)    
        garment.calculate_total_time()
        garments_list.append(garment)
        
    print("Select a garment to start production:")
    for idx, garment in enumerate(garments_list):
        print(f"{idx + 1}. Garment: {garment.name}")

    selected_idx = int(input("Enter the number of the garment to start production: ")) - 1
    selected_garment = garments_list[selected_idx]
    
    print("How many garments are in production?")
    quantity = int(input())

    print("Available operations:")
    for idx, operation in enumerate(selected_garment.operations):
        print(f"{idx + 1}. Operation: {operation}")

    selected_operation_idx = int(input("Enter the number of the operation to perform: ")) - 1
    selected_operation = list(selected_garment.operations.keys())[selected_operation_idx]

   
    print(f"Garment selected for production: {selected_garment.name}")
    
    print(f"Total Time for {selected_garment.name}: {float(selected_garment.total_time) * quantity} minutes")
    print(f"Operation selected: {selected_operation}")
    selected_operation_time = selected_garment.operations[selected_operation]
    print(f"Total time for this operation: {selected_operation_time} minutes")

    production = selected_operation_time * quantity
    print(f"Total production time for {quantity} {selected_operation}: {production} minutes")

    
    completed_operations = 0
    start_time = time.time()

    while completed_operations < production:
        input("Press Enter when an operation is completed:")
        completed_operations += 1

        elapsed_time = time.time() - start_time
        time_per_operation = elapsed_time / completed_operations if completed_operations > 0 else 0
        remaining_operations = production - completed_operations
        time_remaining = remaining_operations * time_per_operation

        print(f"Operations completed: {completed_operations}/{production}")
        print(f"Elapsed time: {elapsed_time:.2f} seconds")
        print(f"Estimated time remaining: {time_remaining:.2f} seconds")




main_app()
