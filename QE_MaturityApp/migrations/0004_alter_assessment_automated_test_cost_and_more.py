# Generated by Django 4.2.13 on 2024-05-28 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QE_MaturityApp', '0003_assessment_question_1_assessment_question_10_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='automated_test_cost',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='automated_tests',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='manual_test_cost',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='manual_tests',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='question_1',
            field=models.IntegerField(choices=[(0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity')], default=0),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='question_10',
            field=models.IntegerField(choices=[(0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity')], default=0),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='question_11',
            field=models.IntegerField(choices=[(0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity')], default=0),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='question_12',
            field=models.IntegerField(choices=[(0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity')], default=0),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='question_13',
            field=models.IntegerField(choices=[(0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity')], default=0),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='question_14',
            field=models.IntegerField(choices=[(0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity')], default=0),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='question_2',
            field=models.IntegerField(choices=[(0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity')], default=0),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='question_3',
            field=models.IntegerField(choices=[(0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity')], default=0),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='question_4',
            field=models.IntegerField(choices=[(0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity')], default=0),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='question_5',
            field=models.IntegerField(choices=[(0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity')], default=0),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='question_6',
            field=models.IntegerField(choices=[(0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity')], default=0),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='question_7',
            field=models.IntegerField(choices=[(0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity')], default=0),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='question_8',
            field=models.IntegerField(choices=[(0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity')], default=0),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='question_9',
            field=models.IntegerField(choices=[(0, 'No Maturity'), (1, 'Low Maturity'), (2, 'Good Maturity'), (3, 'High Maturity')], default=0),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='resource_count',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='resource_type',
            field=models.CharField(choices=[('permanent', 'Permanent'), ('contractor', 'Contractor')], max_length=10),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='test_cases_executed',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='test_execution_days',
            field=models.IntegerField(),
        ),
    ]
