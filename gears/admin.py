from django.contrib import admin
from .models import Gear


@admin.register(Gear)
class GearAdmin(admin.ModelAdmin):
    list_display = ('module', 'tooth_count', 'material', 'pitch_diameter', 'created_at')
    list_filter = ('material',)
    ordering = ('-created_at',)