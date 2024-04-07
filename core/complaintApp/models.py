from django.db import models

from account.models import User

# Create your models here.

class Griv(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    PREFERRED_RESOLUTION_CHOICES = [
        ('immediate_resolution', 'Immediate resolution'),
        ('investigation_required', 'Investigation required'),
        ('follow_up_required', 'Follow-up required'),
    ]

    STATUS_CHOICES = [
        (0, 'Pending'),
        (1, 'Resolved'),
    ]

    GRIEVANCE_CATEGORIES = [
        ('road_conditions', 'Road Conditions'),
        ('water_supply', 'Water Supply'),
        ('electricity', 'Electricity'),
        ('payment_issues', 'Payment Issues'),
        ('noise_disputes', 'Noise Disputes'),
        ('other', 'Other (please specify)'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES,default='male')
    grievance_category = models.CharField(max_length=20, choices=GRIEVANCE_CATEGORIES)
    grievance_description = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    preferred_resolution = models.CharField(max_length=30, choices=PREFERRED_RESOLUTION_CHOICES)
    target_language = models.CharField(max_length=2, choices=[('en', 'English'), ('mr', 'Marathi'), ('hi', 'Hindi')], default='en')
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)
    submit_date = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return f"Griv #{self.id}"