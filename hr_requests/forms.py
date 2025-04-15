from django import forms
from .models import HRRequest

class HRRequestForm(forms.ModelForm):
    class Meta:
        model = HRRequest
        fields = ['employee_name', 'employee_id']