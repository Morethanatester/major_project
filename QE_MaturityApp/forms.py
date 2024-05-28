from django import forms
from .models import *


class BaselineForm(forms.Form):
    total_resource_permanent = forms.IntegerField(label='Total Permanent Resources', min_value=0)
    total_resource_contractor = forms.IntegerField(label='Total Contractor Resources', min_value=0)
    total_test_cases = forms.IntegerField(label='Total Test Cases', min_value=0)
    total_execution_time_days = forms.IntegerField(label='Total Execution Time (Days)', min_value=0)

    def clean(self):
        cleaned_data = super().clean()
        total_resource_permanent = cleaned_data.get("total_resource_permanent")
        total_resource_contractor = cleaned_data.get("total_resource_contractor")
        total_test_cases = cleaned_data.get("total_test_cases")
        total_execution_time_days = cleaned_data.get("total_execution_time_days")
        
        # Check if all fields are 0
        if total_resource_permanent == total_resource_contractor == total_test_cases == total_execution_time_days == 0:
            raise forms.ValidationError("Please enter values greater than 0 for at least one field.")