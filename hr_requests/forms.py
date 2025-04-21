from django import forms
from .models import HRRequest

class HRRequestForm(forms.ModelForm):
    class Meta:
        model = HRRequest
        fields = ['employee_name', 'employee_id', 'photo']
        
    def __init__(self, *args, **kwargs):
        request_type = kwargs.pop('request_type', None)
        super().__init__(*args, **kwargs)
        
        if request_type != 'vacation':
            self.fields.pop('photo')