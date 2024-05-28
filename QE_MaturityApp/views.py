from django.shortcuts import render, redirect
from .forms import BaselineForm, AssessmentForm
from .models import Assessment

def home(request):
    return render(request, "home.html", {})

def QEMaturity(request):
    return render(request, "QEMaturity.html", {})

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

                # Round the results to 2 decimal places
                total_cost = round(total_cost, 2)
                cost_per_test = round(cost_per_test, 2)

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


#****Assessment*****
def maturity_assessment(request):
    print('maturity_assessment function called')
    if request.method == 'POST':
        form = AssessmentForm(request.POST)
        if form.is_valid():
            print('Form cleaned data:', form.cleaned_data)  # Print form.cleaned_data
            # Process the form data and calculate new scores
            new_total_cost, new_cost_per_test = calculate_new_scores(request, form.cleaned_data)  # Switched order of arguments
            # Store results in session variables
            request.session['new_total_cost'] = new_total_cost
            request.session['new_cost_per_test'] = new_cost_per_test
            # Pass the new scores to the template
            return render(request, 'maturity.html', {'new_total_cost': new_total_cost, 'new_cost_per_test': new_cost_per_test})
        else:
            print('Form errors:', form.errors)
            return render(request, 'maturity.html', {'form': form})  # Pass the form with errors back to the template
    else:
        form = AssessmentForm()
    return render(request, 'maturity.html', {'form': form})

def calculate_new_scores(request, form_data):
    COST_REDUCTION_PERCENTAGES = {
        range(0, 15): 1.0,  # No Maturity = 100% of original cost
        range(15, 30): 0.8,  # Low Maturity = 80% of original cost
        range(30, 45): 0.6,  # Good Maturity = 60% of original cost
        range(45, 61): 0.4   # High Maturity/Continuous Maturity = 40% of original cost
    }
    
    # Calculate total maturity level by summing up the answers to all 14 questions
    total_maturity_level = sum(int(form_data.get(f'question_{i}', 0)) for i in range(1, 15))
    
    # Map the total maturity level to a cost reduction percentage
    for range_, percentage in COST_REDUCTION_PERCENTAGES.items():
        if total_maturity_level in range_:
            cost_reduction_percentage = percentage
            break
    else:
        cost_reduction_percentage = 1.0  # Default to 100% if total_maturity_level is not in any range
    
    # For debugging purposes, print the calculated values
    print("Total Maturity Level:", total_maturity_level)
    print("Cost Reduction Percentage:", cost_reduction_percentage)
    
    # Assuming original total cost and cost per test are retrieved from session
    original_total_cost = request.session.get('total_cost', 0)
    original_cost_per_test = request.session.get('cost_per_test', 0)
    
    new_total_cost = original_total_cost * cost_reduction_percentage
    new_cost_per_test = original_cost_per_test * cost_reduction_percentage
    
    # For debugging purposes, print the new scores
    print("New Total Cost:", new_total_cost)
    print("New Cost Per Test:", new_cost_per_test)
    
    return new_total_cost, new_cost_per_test
def maturity(request):
    print('maturity function called')
    print('Request method:', request.method)
    return render(request, "maturity.html", {})