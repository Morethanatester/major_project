from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import TestAssessmentForm
from .models import TestAssessment

def calculate_costs(num_test_cases, num_resources):
    manual_testing_cost_per_case = 50  # Example cost
    automated_testing_cost_per_case = 10  # Example cost
    resource_cost_per_case = 5  # Example cost per resource

    manual_testing_cost = num_test_cases * manual_testing_cost_per_case
    automated_testing_cost = num_test_cases * automated_testing_cost_per_case
    total_resource_cost = num_resources * resource_cost_per_case

    return manual_testing_cost + total_resource_cost, automated_testing_cost + total_resource_cost

def test_assessment_view(request):
    if request.method == 'POST':
        form = TestAssessmentForm(request.POST)
        if form.is_valid():
            assessment = form.save(commit=False)
            manual_cost, automated_cost = calculate_costs(assessment.num_test_cases, assessment.num_resources)
            assessment.manual_testing_cost = manual_cost
            assessment.automated_testing_cost = automated_cost
            assessment.save()
            return redirect('assessment_result', pk=assessment.pk)
    else:
        form = TestAssessmentForm()

    return render(request, 'test_assessment_form.html', {'form': form})

def assessment_result_view(request, pk):
    assessment = TestAssessment.objects.get(pk=pk)
    return render(request, 'assessment_result.html', {'assessment': assessment})

def home(request):
    return render(request, "home.html", {})