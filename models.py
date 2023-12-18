class Garment:
    def __init__(self, name, total_time=0, total_operations=0):
        self.name = name
        self.total_time = total_time
        self.operations = {}
        self.total_operations = total_operations
        
    def append_operations(self, operation, time_allowed):
        self.operations[operation] = time_allowed
    
    def calculate_total_time(self):
        self.total_time = sum(self.operations.values())
        
    #def calculate_total_operations(self, total_number_of_operations):
    #    self.total_operations = total_number_of_operations