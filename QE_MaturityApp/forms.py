# assessment/forms.py
from django import forms
from .models import TestAssessment

class TestAssessmentForm(forms.ModelForm):
    class Meta:
        model = TestAssessment
        fields = ['project_name', 'num_test_cases', 'num_resources', 'test_type', 'manual_testing_cost', 'automated_testing_cost']