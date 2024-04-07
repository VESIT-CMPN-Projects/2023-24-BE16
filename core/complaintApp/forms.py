# village_info_system/grievance/forms.py

from django import forms
from .models import Griv

class GrievanceForm(forms.ModelForm):
    class Meta:
        model = Griv
        fields = ['contact_number', 'address', 'gender', 'grievance_category',
                  'grievance_description', 'attachment', 'preferred_resolution', 'target_language']
