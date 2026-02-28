from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.

LOCATION_CHOICES = [
    ('Select', 'Select'),
    ('Spanish Town', 'Spanish Town'),
    ('Greater Portmore', 'Greater Portmore'),
    ('Old Harbour', 'Old Harbour'),
    ('St. Jago Park','St. Jago Park'),
    ('Linstead', 'Linstead'),
]

ISSUE_TYPES = [
    ('Select', 'Select'),
    ('Carpentry', 'Carpentry'),
    ('Electrical', 'Electrical'),
    ('Masonry', 'Masonry'),
    ('Plumbing', 'Plumbing'),
    ('Air Conditioning', 'Air Conditioning'),
    ('Other', 'Other'),
]

PRIORITY_LEVELS = [
    ('Select', 'Select'),
    ('Low', 'Low'),
    ('Medium', 'Medium'),
    ('High', 'High'),
    ('Critical', 'Critical'),
]

STATUS_CHOICES = [
    ('Open', 'Open'),
    ('Verified', 'Verified'),
    ('Assigned', 'Assigned'),
    ('Closed', 'Closed'),
]


class Report(models.Model):
    full_name = models.CharField(
        max_length=100,
        verbose_name="Reporter's Full Name",
        default="",
    )
    email = models.EmailField(
        verbose_name="Reporter's Email",
        default=""
    )
    phone_number = models.CharField(
        max_length=20,
        verbose_name="Contact Phone",
        blank=True,  # Makes field optional
        null=True,
        default=""
    )
    reporter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reported_issues', default="")
    location = models.CharField(max_length=255, choices= LOCATION_CHOICES, default='Select')
    department = models.CharField(max_length=255, default="")
    issue_type = models.CharField(max_length=255, choices=ISSUE_TYPES, default='Select')
    description = models.TextField(default="", blank=True)
    priority_level = models.CharField(max_length=255, choices= PRIORITY_LEVELS, default='Select')
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='Open')
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_issues')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    resolution_notes = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"Report #{self.id} - {self.get_issue_type_display()} at {self.get_location_display()}"
    
    class Meta:
        ordering = ['-created_at']

    
 