class Garment:
    def __init__(self, name, total_time=0):
        self.name = name
        self.total_time = total_time
        self.operations = {}
        
    def append_operations(self, operation, time_allowed):
        self.operations[operation] = time_allowed
    
    def calculate_total_time(self):
        self.total_time = sum(self.operations.values())