from django.db import models

class Garment(models.Model):
    
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Operation(models.Model):
    garment_name = models.ForeignKey(Garment, on_delete=models.CASCADE)
    operation_name = models.CharField(max_length=100)
    time_allowed = models.FloatField()
    
    def __str__(self):
        return self.operation_name
    