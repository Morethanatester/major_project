# Generated by Django 4.2.13 on 2024-05-26 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestAssessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('num_test_cases', models.IntegerField()),
                ('num_resources', models.IntegerField()),
                ('test_type', models.CharField(max_length=200)),
                ('manual_testing_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('automated_testing_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
    ]
