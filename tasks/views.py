from django.shortcuts import render, redirect, get_object_or_404
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
    
def edit_job(request,id):
    selected_job = get_object_or_404(Job_detail, pk=id)
    
    if request.method == "POST":
        form = Job_form(request.POST, request.FILES, instance=selected_job)
        if form.is_valid():
            form.user = request.user
            form.save()
            return redirect(profile)
    else:
        form = Job_form(instance=selected_job)
        return render(request, 'edit_job.html',{
            'form':form,
            'data':selected_job,
            'id': id,
        })
