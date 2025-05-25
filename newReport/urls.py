from django.urls import path
from . import views

app_name = 'newReport'

urlpatterns = [
    path('view-report/', views.view_report, name='view_report'),
] 