from django.shortcuts import render, redirect
from hands.forms import NewHand
from accounts.views import index

# Create your views here.
def hand_list(request):
    return render(request, 'hand_list.html')

def hand_profile(request):
    if request.method == "POST":
        form = NewHand(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
        return redirect(index)
    else:   
        form = NewHand()
        return render(request, 'hand_profile.html',{
            'form' : form
    })