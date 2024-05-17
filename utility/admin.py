from django.contrib import admin
from .models import Meter, Meter_Data
# Register your models here.

class Meter_Data_Inline(admin.TabularInline):
    model = Meter_Data
    extra = 0

@admin.register(Meter)
class MetersAdmin(admin.ModelAdmin):
    inlines = [Meter_Data_Inline]
    list_display = ('label','modified_data')

    def modified_data(self, obj):
        latest_meter_data = obj.meters.order_by('-modified').first()
        if latest_meter_data:
            return latest_meter_data.modified
        return None
    
    modified_data.admin_order_field = 'meters__modified'
    modified_data.short_description = 'Latest Modified'

@admin.register(Meter_Data)
class Meter_Data_Admin(admin.ModelAdmin):
    list_display = ('id','value','created','modified')