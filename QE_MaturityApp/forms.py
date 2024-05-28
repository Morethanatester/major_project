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
        

class AssessmentForm(forms.Form):
    question_1 = forms.ChoiceField(label="Do you follow an integrated SE/QE development approach?", choices=((0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity/Continuous Maturity')), error_messages={'required': 'Please answer this question.'})
    question_2 = forms.ChoiceField(label="Do all Quality Engineers write code for interviews?", choices=((0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity/Continuous Maturity')), error_messages={'required': 'Please answer this question.'})
    question_3 = forms.ChoiceField(label="Do you have a Quality Engineering Principles in place (MVE)?", choices=((0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity/Continuous Maturity')), error_messages={'required': 'Please answer this question.'})
    question_4 = forms.ChoiceField(label="Do you continue to follow your principles even when you have a tight deadline?", choices=((0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity/Continuous Maturity')), error_messages={'required': 'Please answer this question.'})
    question_5 = forms.ChoiceField(label="Are new tests automated from Unit to Release?", choices=((0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity/Continuous Maturity')), error_messages={'required': 'Please answer this question.'})
    question_6 = forms.ChoiceField(label="Are E2E tests Embedded as part of your CI/CD?", choices=((0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity/Continuous Maturity')), error_messages={'required': 'Please answer this question.'})
    question_7 = forms.ChoiceField(label="Are non-functional test run as part of CI/CD?", choices=((0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity/Continuous Maturity')), error_messages={'required': 'Please answer this question.'})
    question_8 = forms.ChoiceField(label="Are all key workflows automated?", choices=((0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity/Continuous Maturity')), error_messages={'required': 'Please answer this question.'})
    question_9 = forms.ChoiceField(label="Is your Test Data generation automated?", choices=((0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity/Continuous Maturity')), error_messages={'required': 'Please answer this question.'})
    question_10 = forms.ChoiceField(label="Do you have the best tools available to support?", choices=((0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity/Continuous Maturity')), error_messages={'required': 'Please answer this question.'})
    question_11 = forms.ChoiceField(label="Are your Environment builds automated?", choices=((0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity/Continuous Maturity')), error_messages={'required': 'Please answer this question.'})
    question_12 = forms.ChoiceField(label="Do you monitor Env activity and run synthetic health checks in Env?", choices=((0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity/Continuous Maturity')), error_messages={'required': 'Please answer this question.'})
    question_13 = forms.ChoiceField(label="Do you have Automated Test Reporting and MI?", choices=((0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity/Continuous Maturity')), error_messages={'required': 'Please answer this question.'})
    question_14 = forms.ChoiceField(label="Do you have a QE Dashboard that is used by all stakeholders?", choices=((0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity/Continuous Maturity')), error_messages={'required': 'Please answer this question.'})