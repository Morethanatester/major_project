from django.test import TestCase, Client
from django.urls import reverse
from QE_MaturityApp.forms import BaselineForm, AssessmentForm
from QE_MaturityApp.views import calculate_total_cost, calculate_new_scores
import time

class ViewTests(TestCase):
    
    def setUp(self):
        self.client = Client()

    # Functional Tests
    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_QEMaturity_page(self):
        response = self.client.get(reverse('QEMaturity'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'QEMaturity.html')

    def test_baseline_page_get(self):
        response = self.client.get(reverse('baseline'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'assessment.html')
        self.assertIsInstance(response.context['form'], BaselineForm)

    def test_baseline_page_post(self):
        form_data = {
            'total_resource_permanent': 5,
            'total_resource_contractor': 3,
            'total_test_cases': 100,
            'total_execution_time_days': 10
        }
        response = self.client.post(reverse('baseline'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'assessment.html')
        self.assertIn('total_cost', response.context)
        self.assertIn('cost_per_test', response.context)

    def test_maturity_assessment_page_get(self):
        response = self.client.get(reverse('maturity_assessment'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'maturity.html')
        self.assertIsInstance(response.context['form'], AssessmentForm)

    def test_maturity_assessment_page_post(self):
        # First, set up the session with initial baseline data
        session = self.client.session
        session['total_cost'] = 10000
        session['cost_per_test'] = 100
        session['total_execution_time_days'] = 10
        session.save()
        
        form_data = {f'question_{i}': 2 for i in range(1, 15)}
        form_data['num_executions'] = 5
        response = self.client.post(reverse('maturity_assessment'), data=form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'maturity.html')
        self.assertIn('new_total_cost', response.context)
        self.assertIn('new_cost_per_test', response.context)
        self.assertIn('cost_savings', response.context)
        self.assertIn('time_saved', response.context)

    def test_blog1_page(self):
        response = self.client.get(reverse('blog1'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog1.html')

    def test_blog2_page(self):
        response = self.client.get(reverse('blog2'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog2.html')

    # Unit Tests for Helper Functions
    def test_calculate_total_cost(self):
        total_resource_permanent = 5
        total_resource_contractor = 3
        total_test_cases = 100
        total_execution_time_days = 10
        
        expected_total_cost = (5 * 454 + 3 * 1400) * 10
        self.assertEqual(calculate_total_cost(total_resource_permanent, total_resource_contractor, total_test_cases, total_execution_time_days), expected_total_cost)

    def test_calculate_new_scores_no_maturity(self):
        request = self.client.request().wsgi_request
        request.session['total_cost'] = 10000
        request.session['cost_per_test'] = 100
        request.session['total_execution_time_days'] = 10
        
        form_data = {f'question_{i}': 1 for i in range(1, 15)}
        form_data['num_executions'] = 5
        
        new_total_cost, new_cost_per_test, cost_savings, time_saved, maturity_level = calculate_new_scores(request, form_data)
        
        self.assertEqual(new_total_cost, 10000)
        self.assertEqual(new_cost_per_test, 100)
        self.assertEqual(cost_savings, 0)
        self.assertEqual(time_saved, 0)
        self.assertEqual(maturity_level, 'No Maturity')

    def test_calculate_new_scores_high_maturity(self):
        request = self.client.request().wsgi_request
        request.session['total_cost'] = 10000
        request.session['cost_per_test'] = 100
        request.session['total_execution_time_days'] = 10
        
        # Form data representing high maturity (14 questions with a score of 5 each)
        form_data = {f'question_{i}': 5 for i in range(1, 15)}  # This should total 70 (5*14), which falls into "High Maturity"
        form_data['num_executions'] = 5
        
        new_total_cost, new_cost_per_test, cost_savings, time_saved, maturity_level = calculate_new_scores(request, form_data)
        
        print(f"New Total Cost: {new_total_cost}")
        print(f"New Cost Per Test: {new_cost_per_test}")
        print(f"Cost Savings: {cost_savings}")
        print(f"Time Saved: {time_saved}")
        print(f"Maturity Level: {maturity_level}")
        
        self.assertEqual(new_total_cost, 4000)  # 40% of original cost
        self.assertEqual(new_cost_per_test, 40)  # 40% of original cost per test
        self.assertEqual(cost_savings, 30000)  # 6000 * 5
        self.assertEqual(time_saved, 30)  # 10 * 0.6 * 5
        self.assertEqual(maturity_level, 'High Maturity')

    # Non-functional Tests
    def test_baseline_page_post_security(self):
        # Test for SQL Injection (this is a simple example, for real-world cases use more sophisticated methods)
        form_data = {
            'total_resource_permanent': "1; DROP TABLE users;",
            'total_resource_contractor': 3,
            'total_test_cases': 100,
            'total_execution_time_days': 10
        }
        response = self.client.post(reverse('baseline'), data=form_data)
        self.assertNotEqual(response.status_code, 500)  # Should not result in a server error

    def test_performance_baseline_page(self):
        start_time = time.time()
        for _ in range(100):
            response = self.client.get(reverse('baseline'))
            self.assertEqual(response.status_code, 200)
        end_time = time.time()
        duration = end_time - start_time
        self.assertLess(duration, 2)  # Ensure 100 requests take less than 2 seconds
