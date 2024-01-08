from django.contrib import admin
from .models import Garment, Operation

class OperationInline(admin.TabularInline):
    model = Operation

@admin.register(Garment)
class GarmentAdmin(admin.ModelAdmin):
    inlines = [
        OperationInline,
    ]

admin.site.register(Operation)  # Optional, as it's already registered above
