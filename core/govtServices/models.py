from django.db import models

# Create your models here.
class saveService(models.Model):
    service_name = models.CharField(max_length=100)
    service_description = models.CharField(max_length=1000)
    service_contact = models.CharField(max_length=50)