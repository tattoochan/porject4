from django.urls import path, include
from hands.views import hand_list, hand_profile, edit_profile, delete_profile, confirm_delete_profile

urlpatterns = [
    path('', hand_list, name='hand_list'),
    path('hand_profile/', hand_profile, name='hand_profile'),
    path('edit_profile/<id>', edit_profile, name='edit_profile'),
    path('delete_profile/<id>', delete_profile, name='delete_profile'),
    path('confirm_delete_profile/<id>', confirm_delete_profile, name='confirm_delete_profile'),
]