from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Garment(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.FloatField(default=0)
    progress = models.FloatField(default=0.0)

    def calculate_total_time(self):
        total_time = 0
        for operation in self.operation_set.all():
            total_time += operation.total_time
        return total_time

    def __str__(self):
        return self.name

class Operation(models.Model):
    garment = models.ForeignKey(Garment, on_delete=models.CASCADE)
    operation_name = models.CharField(max_length=100)
    time_allowed = models.FloatField()

    @property
    def total_time(self):
        return self.garment.quantity * self.time_allowed

    def __str__(self):
        return self.operation_name
    
class OperationRecord(models.Model):
    garment = models.ForeignKey('Garment', on_delete=models.CASCADE)
    operation = models.ForeignKey('Operation', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    elapsed_time = models.FloatField()
    efficiency = models.FloatField()
    progress_percentage = models.FloatField()

    def __str__(self):
        return f"Record for {self.garment.name} - {self.operation.operation_name}"

# Example usage
# my_garment = Garment.objects.get(id=1)
# total_time_for_garment = my_garment.calculate_total_time()
# print(total_time_for_garment)
