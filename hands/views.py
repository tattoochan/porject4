from django.shortcuts import render, redirect, get_object_or_404
from hands.forms import NewHand
from hands.models import Hands_info
from accounts.views import index

# Create your views here.
def hand_list(request):
    result = Hands_info.objects.all()
    return render(request, 'hand_list.html', {
        'data' : result
    })

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
    
def edit_profile (request,id):

    return render(request, 'edit_profile.html',{
        # 'form':form
    })
    