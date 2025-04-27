from django import forms
from .models import Meal

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['name', 'description', 'price', 'time', 'image']
        widgets = {
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }