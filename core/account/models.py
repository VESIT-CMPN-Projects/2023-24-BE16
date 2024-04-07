from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_user = models.BooleanField('Is user', default=True)
    is_approved = models.BooleanField(default=False)


    # Document verification fields
    aadhaar_card_image = models.ImageField(upload_to='documents/', null=True, blank=True)
    pan_card_image = models.ImageField(upload_to='documents/', null=True, blank=True)
    proof_of_address_electricity_image = models.ImageField(upload_to='documents/', null=True, blank=True)
    income_certificate_image = models.ImageField(upload_to='documents/', null=True, blank=True)
    bpl_ration_card_image = models.ImageField(upload_to='documents/', null=True, blank=True)

    aadhaar_card_text = models.CharField(max_length=255, null=True, blank=True)
    pan_card_text = models.CharField(max_length=255, null=True, blank=True)
    proof_of_address_electricity_text = models.CharField(max_length=255, null=True, blank=True)
    income_certificate_text = models.CharField(max_length=255, null=True, blank=True)
    bpl_ration_card_text = models.CharField(max_length=255, null=True, blank=True)

    def has_verified_documents(self):
        # Check if all required document verification fields are filled
        return all(getattr(self, f"{field}_image") for field in ['aadhaar_card', 'pan_card'])

    
    