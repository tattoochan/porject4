from django.shortcuts import render, redirect
from tasks.models import Job_detail
from tasks.forms import Job_form
from hands.views import profile

# Create your views here.
def job_listing(request):
    return render(request, 'job_listing.html')
    
def add_job(request):
    if request.method == "POST":
        form = Job_form(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
        return redirect(profile)
    else:   
        form = Job_form()
        return render(request, 'add_job.html',{
            'form' : form
    })
    
