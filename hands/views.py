from django.shortcuts import render, redirect, get_object_or_404
from hands.forms import Profile_form
from hands.models import Hands_info
from accounts.views import index
from tasks.models import Job_detail

# Create your views here.
""" Display all the listings """
def help_list(request):
    result = Hands_info.objects.all()
    return render(request, 'help_list.html', {
        'data' : result
    })

""" Display the profile """
def profile(request):
    # result = Hands_info.objects.all()
    hand_result = Hands_info.objects.filter(user = request.user )
    job_result = Job_detail.objects.filter(user = request.user)
    if len(hand_result) == 0 :
        return redirect(add_profile)
    return render(request, 'profile.html', {
        'data' : hand_result[0],
        'data2': job_result,
    })

""" Entry for New profile """
def add_profile(request): 
    result = Hands_info.objects.filter(user = request.user )
    if len(result) > 0 :
        return redirect(profile)
        
    if request.method == "POST":
        form = Profile_form(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
        return redirect(profile)
    else:   
        form = Profile_form()
        return render(request, 'add_profile.html',{
            'form' : form
    })
    
""" Edit for Existing profile"""    
def edit_profile (request,id):
    selected_profile = get_object_or_404(Hands_info, pk=id)
    
    if request.method == "POST":
        form = Profile_form(request.POST, request.FILES, instance=selected_profile)
        if form.is_valid():
            form.user = request.user
            form.save()
            return redirect(profile)
    else:
        form = Profile_form(instance=selected_profile)
    
        return render(request, 'edit_profile.html',{
            'form':form
        })
    
def delete_profile(request, id):
    selected_profile = get_object_or_404(Hands_info, pk=id)
    return render(request, 'delete_profile.html',{
        'data': selected_profile
    })
    
def confirm_delete_profile(request,id):
    Hands_info.objects.filter(pk=id).delete()
    return redirect(profile)