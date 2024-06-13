from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page with the assessment form
    path('QEMaturity/', views.QEMaturity, name='QEMaturity'),
    path('baseline/', views.baseline, name='baseline'),
    path('maturity/', views.maturity, name='maturity'),
    path('maturity_assessment/', views.maturity_assessment, name='maturity_assessment'),

    path('blog1/', views.blog1, name='blog1'),
    path('blog2/', views.blog2, name='blog2'),

]