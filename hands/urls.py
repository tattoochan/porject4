from django.urls import path, include
from hands.views import profile, add_profile, edit_profile, delete_profile, confirm_delete_profile, help_list

urlpatterns = [
    path('profile/', profile, name='profile'),
    path('help_list/', help_list, name='help_list'),
    path('add_profile/', add_profile, name='add_profile'),
    path('edit_profile/<id>', edit_profile, name='edit_profile'),
    path('delete_profile/<id>', delete_profile, name='delete_profile'),
    path('confirm_delete_profile/<id>', confirm_delete_profile, name='confirm_delete_profile'),
]