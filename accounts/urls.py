from django.urls import path, include
from accounts.views import index, logout

urlpatterns = [
    path('', index, name='index'),
    path('logout/', logout, name='logout'),
]