from django.urls import path
from QE_MaturityApp import views

urlpatterns = [
    path("", views.home, name="home"),
]