from django.shortcuts import render, redirect
from .forms import BaselineForm
from .models import Assessment

def home(request):
    return render(request, "home.html", {})

def baseline(request):
    total_cost = None
    cost_per_test = None
    
    if request.method == 'POST':
        form = BaselineForm(request.POST)
        if form.is_valid():
            total_resource_permanent = form.cleaned_data['total_resource_permanent']
            total_resource_contractor = form.cleaned_data['total_resource_contractor']
            total_test_cases = form.cleaned_data['total_test_cases']
            total_execution_time_days = form.cleaned_data['total_execution_time_days']
            
            if total_resource_permanent == 0 and total_resource_contractor == 0:
                form.add_error(None, 'Total resources cannot be zero.')
            else:
                total_cost = calculate_total_cost(total_resource_permanent, total_resource_contractor, total_test_cases, total_execution_time_days)
                cost_per_test = total_cost / total_test_cases if total_test_cases != 0 else 0

                # Store results in session variables
                request.session['total_cost'] = total_cost
                request.session['cost_per_test'] = cost_per_test
        else:
            form.add_error(None, 'All values must be greater than or equal to 0.')
    else:
        form = BaselineForm()

    context = {
        'form': form,
        'total_cost': total_cost,
        'cost_per_test': cost_per_test
    }

    return render(request, 'assessment.html', context)

def calculate_total_cost(total_resource_permanent, total_resource_contractor, total_test_cases, total_execution_time_days):
    COST_PER_RESOURCE_PERMANENT = 454
    COST_PER_RESOURCE_CONTRACTOR = 1400

    total_cost = (total_resource_permanent * COST_PER_RESOURCE_PERMANENT) + (total_resource_contractor * COST_PER_RESOURCE_CONTRACTOR)
    total_cost *= total_execution_time_days

    return total_cost