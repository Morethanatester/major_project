from django.shortcuts import render, redirect
from .forms import BaselineForm, AssessmentForm
from .models import Assessment

# This view function renders the home page.
def home(request):
    return render(request, "home.html", {})

# This view function renders the QEMaturity page.
def QEMaturity(request):
    return render(request, "QEMaturity.html", {})

# This view function handles the baseline form submission and calculation.
# It calculates the total cost and cost per test based on the form inputs.
# The results are stored in session variables and passed to the context for rendering.
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
                request.session['total_execution_time_days'] = total_execution_time_days  # Store total_execution_time_days in session
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


# This function calculates the total cost based on the provided resources, test cases, and execution time.
# It uses predefined costs for permanent and contractor resources.
def calculate_total_cost(total_resource_permanent, total_resource_contractor, total_test_cases, total_execution_time_days):
    COST_PER_RESOURCE_PERMANENT = 454
    COST_PER_RESOURCE_CONTRACTOR = 1400

    total_cost = (total_resource_permanent * COST_PER_RESOURCE_PERMANENT) + (total_resource_contractor * COST_PER_RESOURCE_CONTRACTOR)
    total_cost *= total_execution_time_days

    return total_cost

# This view function handles the maturity assessment process.
# It takes in the request object as a parameter.
# Depending on the request method (GET or POST), it either renders the assessment form or processes the form data.
def maturity_assessment(request):
    if request.method == 'POST':
        form = AssessmentForm(request.POST)
        if form.is_valid():
            # Process the form data and calculate new scores
            new_total_cost, new_cost_per_test, cost_savings, time_saved, total_maturity_level  = calculate_new_scores(request, form.cleaned_data)  # Switched order of arguments
            # Store results in session variables
            request.session['new_total_cost'] = new_total_cost
            request.session['new_cost_per_test'] = new_cost_per_test
            request.session['new_total_cost'] = new_total_cost
            request.session['new_cost_per_test'] = new_cost_per_test
            request.session['cost_savings'] = cost_savings
            request.session['time_saved'] = time_saved
            # Pass the new scores to the template
                # Pass the new scores and total_maturity_level to the template
            return render(request, 'maturity.html', {
                'new_total_cost': new_total_cost, 
                'new_cost_per_test': new_cost_per_test, 
                'cost_savings': cost_savings, 
                'time_saved': time_saved,
                'total_maturity_level': total_maturity_level
            })
        else:
            print('Form errors:', form.errors)
            return render(request, 'maturity.html', {'form': form})  # Pass the form with errors back to the template
    else:
        form = AssessmentForm()
    return render(request, 'maturity.html', {'form': form})


# This view function handles the calculation of new scores based on the form data.
# It takes in the request object and the form data as parameters.
# The form data is processed and the new scores are calculated and returned.
def calculate_new_scores(request, form_data):
    COST_REDUCTION_PERCENTAGES = {
        range(0, 15): (1.0, "No Maturity"),  # No Maturity = 100% of original cost
        range(15, 29): (0.8, "Low Maturity"),  # Low Maturity = 80% of original cost
        range(29, 39): (0.6, "Good Maturity"),  # Good Maturity = 60% of original cost
        range(39, 61): (0.4, "High Maturity")   # High Maturity/Continuous Maturity = 40% of original cost
    }
    
    # Calculate total maturity level by summing up the answers to all 14 questions
    total_maturity_level = sum(int(form_data.get(f'question_{i}', 0)) for i in range(1, 15))

    # Map the total maturity level to a cost reduction percentage and a maturity level description
    for range_, (percentage, maturity_level) in COST_REDUCTION_PERCENTAGES.items():
        if total_maturity_level in range_:
            cost_reduction_percentage = percentage
            break
    else:
        cost_reduction_percentage = 1.0  # Default to 100% if total_maturity_level is not in any range
        maturity_level = "No Maturity"

    # Assuming original total cost and cost per test are retrieved from session
    original_total_cost = request.session.get('total_cost', 0)
    original_cost_per_test = request.session.get('cost_per_test', 0)

    new_total_cost = round(original_total_cost * cost_reduction_percentage, 2)
    new_cost_per_test = round(original_cost_per_test * cost_reduction_percentage, 2)
    
    # Retrieve the number of test executions from the form data
    num_executions = int(form_data.get('num_executions', 1))

    # Calculate the cost savings and time saved
    cost_savings = (original_total_cost - new_total_cost) * num_executions
    total_execution_time_days = request.session.get('total_execution_time_days', 0)
    time_saved = total_execution_time_days * (1 - cost_reduction_percentage) * num_executions
    
    return new_total_cost, new_cost_per_test, cost_savings, time_saved, maturity_level


def maturity(request):
    return render(request, "maturity.html", {})


def blog1(request):
    return render(request, "blog1.html", {})

def blog2(request):
    return render(request, "blog2.html", {})