# from django.contrib import admin
# from .models import ServiceRequest

# @admin.register(ServiceRequest)
# class ServiceRequestAdmin(admin.ModelAdmin):
#     list_display = ('id', 'customer', 'service_type', 'status', 'submitted_at', 'resolved_at')
#     list_filter = ('status', 'service_type')
#     search_fields = ('customer__username', 'status')

#     def mark_completed(self, request, queryset):
#         queryset.update(status='resolved')
#     mark_completed.short_description = "Mark selected requests as Completed"

#     actions = [mark_completed]


# Register your models here.


from django.contrib import admin
from django.utils.timezone import now
from .models import ServiceRequest

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'service_type', 'status', 'submitted_at', 'resolved_at')
    list_filter = ('status', 'service_type')
    search_fields = ('customer__username', 'status')

    def save_model(self, request, obj, form, change):
        """Automatically update resolved_at when status is changed to 'resolved' or 'cancelled'"""
        if obj.status in ['resolved', 'cancelled'] and not obj.resolved_at:
            obj.resolved_at = now()
        elif obj.status not in ['resolved', 'cancelled']:
            obj.resolved_at = None  # Reset if status changes back
        super().save_model(request, obj, form, change)

    def mark_completed(self, request, queryset):
        """Bulk action: Mark requests as Completed and update resolved_at"""
        queryset.filter(resolved_at__isnull=True).update(status='resolved', resolved_at=now())
    mark_completed.short_description = "Mark selected requests as Completed"

    actions = [mark_completed]



