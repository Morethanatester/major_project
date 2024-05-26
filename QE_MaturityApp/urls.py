from django.urls import path
from QE_MaturityApp import views
from .views import test_assessment_view, assessment_result_view

urlpatterns = [
    path("", views.home, name="home"),
    path('assessment/', views.test_assessment_view, name='test_assessment'),
    path('result/<int:pk>/', views.assessment_result_view, name='assessment_result'),
]