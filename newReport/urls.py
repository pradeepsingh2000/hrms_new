from django.urls import path
from . import views

app_name = 'newReport'

urlpatterns = [
    path('view-report/', views.view_report, name='view_report'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('category/',views.category, name='category'),
    path('create-category/',views.create_category, name='create_category'),
] 