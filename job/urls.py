from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_jobs, name='list_jobs'),
    path('<int:job_id>/', views.job_detail, name='job_detail'),
    path('preview/<int:job_id>/', views.preview_job, name='preview_job'),
    path('create-job/', views.create_job, name="create_job")
]
