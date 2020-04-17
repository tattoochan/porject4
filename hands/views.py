from django.shortcuts import render
# from .models import Hands_info

# Create your views here.
def hand_list(request):
    return render(request, 'hand_list.html')