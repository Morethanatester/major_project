from django.db import models

class TestAssessment(models.Model):
    project_name = models.CharField(max_length=100)
    num_test_cases = models.IntegerField()
    num_resources = models.IntegerField()
    test_type = models.CharField(max_length=200)
    manual_testing_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    automated_testing_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.project_name