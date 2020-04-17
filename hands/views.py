from django.shortcuts import render, redirect, get_object_or_404
from hands.forms import Profile_form
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
        form = Profile_form(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
        return redirect(index)
    else:   
        form = Profile_form()
        return render(request, 'hand_profile.html',{
            'form' : form
    })
    
def edit_profile (request,id):
    selected_profile = get_object_or_404(Hands_info, pk=id)
    
    if request.method == "POST":
        form = Profile_form(request.POST, request.FILES, instance=selected_profile)
        if form.is_valid():
            form.user = request.user
            form.save()
            return redirect(hand_list)
    else:
        form = Profile_form(instance=selected_profile)
    
        return render(request, 'edit_profile.html',{
            'form':form
        })
    