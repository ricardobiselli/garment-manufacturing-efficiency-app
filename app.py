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

    print(f"Garment selected for production: {selected_garment.name}")
    print(f"Total Time for {selected_garment.name}: {selected_garment.total_time} minutes")

    print("How many garments are in production?")
    quantity = int(input())

    production = selected_garment.total_time * quantity
    print(f"Total production time for {quantity} garments: {production} minutes")

    
        


def calculate_expected_time(garment, quantity):
    return garment.total_time * quantity

def check_production_progress(expected_time, start_time, completed_processes):
    elapsed_time = time.time() - start_time
    estimated_completion_time = (expected_time / completed_processes) * (elapsed_time)
    return elapsed_time, estimated_completion_time




main_app()
