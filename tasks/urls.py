from django.urls import path, include
from tasks.views import job_listing, add_job, edit_job

urlpatterns = [
    path('job_listing/', job_listing, name='job_listing'),
    path('add_job/', add_job, name='add_job'),
    path('edit_job/<id>/', edit_job, name='edit_job'),
]