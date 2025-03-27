


# Create your models here.

# from django.db import models
# from django.contrib.auth.models import User

# class ServiceRequest(models.Model):
#     SERVICE_TYPES = [
#         ('installation', 'Installation'),
#         ('repair', 'Repair'),
#         ('inspection', 'Inspection'),
#     ]

#     STATUS_CHOICES = [
#         ('pending', 'Pending'),
#         ('in_progress', 'In Progress'),
#         ('resolved', 'Resolved'),
#         ('cancelled', 'Cancelled')
#     ]

#     customer = models.ForeignKey(User, on_delete=models.CASCADE)
#     service_type = models.CharField(max_length=20, choices=SERVICE_TYPES)
#     description = models.TextField()
#     attachment = models.FileField(upload_to='service_requests/', blank=True, null=True)
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
#     submitted_at = models.DateTimeField(auto_now_add=True)
#     resolved_at = models.DateTimeField(blank=True, null=True)

#     def __str__(self):
#         return f"{self.customer.username} - {self.service_type} - {self.status}"
    

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class ServiceRequest(models.Model):
    SERVICE_TYPES = [
        ('installation', 'Installation'),
        ('repair', 'Repair'),
        ('inspection', 'Inspection'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('cancelled', 'Cancelled')
    ]

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=50)
    description = models.TextField()
    attachment = models.FileField(upload_to='service_requests/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.status in ['resolved', 'cancelled']:
            if not self.resolved_at:  # Ensure resolved_at is only set once
                self.resolved_at = now()
        else:
            self.resolved_at = None  # Reset resolved_at if status is changed back
        
        super().save(*args, **kwargs)  # Save the object

    def __str__(self):
        return f"{self.customer.username} - {self.service_type} - {self.status}"

