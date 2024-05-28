from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page with the assessment form
    path('baseline/', views.baseline, name='baseline'),
    #path('result/<int:assessment_id>/', views.result, name='result'),  # Result page
    #path('result/<int:assessment_id>/<int:total_cost>/', views.result, name='result'),  # Result page with total cost
]