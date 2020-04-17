from django.shortcuts import render
from hands.forms import NewHand

# Create your views here.
def hand_list(request):
    return render(request, 'hand_list.html')

def hand_profile(request):
    form = NewHand()
    return render(request, 'hand_profile.html',{
        'form' : form
    })