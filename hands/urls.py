from django.urls import path, include
from hands.views import hand_list, hand_profile, edit_profile

urlpatterns = [
    path('', hand_list, name='hand_list'),
    path('hand_profile/', hand_profile, name='hand_profile'),
    path('edit_profile/<id>', edit_profile, name='edit_profile'),
]