from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_reports, name='view_reports'),
    path('create/', views.create_report, name='create_report'),
]