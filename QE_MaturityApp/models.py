from django.db import models

class Assessment(models.Model):
    RESOURCE_TYPES = [
        ('permanent', 'Permanent'),
        ('contractor', 'Contractor'),
    ]
    user = models.CharField(max_length=100)
    resource_type = models.CharField(max_length=10, choices=RESOURCE_TYPES)
    test_cases_executed = models.IntegerField()
    test_execution_days = models.IntegerField()
    resource_count = models.IntegerField()
    manual_tests = models.IntegerField()
    automated_tests = models.IntegerField()
    manual_test_cost = models.DecimalField(max_digits=10, decimal_places=2)
    automated_test_cost = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Adding maturity level questions
    question_1 = models.IntegerField(choices=[(0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity')], default=0)
    question_2 = models.IntegerField(choices=[(0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity')], default=0)
    question_3 = models.IntegerField(choices=[(0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity')], default=0)
    question_4 = models.IntegerField(choices=[(0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity')], default=0)
    question_5 = models.IntegerField(choices=[(0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity')], default=0)
    question_6 = models.IntegerField(choices=[(0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity')], default=0)
    question_7 = models.IntegerField(choices=[(0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity')], default=0)
    question_8 = models.IntegerField(choices=[(0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity')], default=0)
    question_9 = models.IntegerField(choices=[(0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity')], default=0)
    question_10 = models.IntegerField(choices=[(0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity')], default=0)
    question_11 = models.IntegerField(choices=[(0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity')], default=0)
    question_12 = models.IntegerField(choices=[(0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity')], default=0)
    question_13 = models.IntegerField(choices=[(0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity')], default=0)
    question_14 = models.IntegerField(choices=[(0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity')], default=0)
