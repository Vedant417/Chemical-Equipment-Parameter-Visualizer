from django.contrib import admin
from .models import EquipmentDataset


@admin.register(EquipmentDataset)
class EquipmentDatasetAdmin(admin.ModelAdmin):
    list_display = (
        'filename',
        'uploaded_at',
        'total_equipment',
        'avg_flowrate',
        'avg_pressure',
        'avg_temperature',
    )
    ordering = ('-uploaded_at',)