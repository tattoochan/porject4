from django.urls import path, include
from accounts.views import index

urlpatterns = [
    path('', index, name='index'),
]