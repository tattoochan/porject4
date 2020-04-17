from django.urls import path, include
from hands.views import hand_list

urlpatterns = [
    path('', hand_list, name='hand_list'),
   
]