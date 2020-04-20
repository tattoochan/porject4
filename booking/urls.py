from django.urls import path, include
from booking.views import booking

urlpatterns = [
    path('<id>/', booking, name='booking'),
]
   