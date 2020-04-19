from django.urls import path, include
from tasks.views import job_listing, add_job

urlpatterns = [
    path('job_listing/', job_listing, name='job_listing'),
    path('add_job/', add_job, name='add_job'),
]