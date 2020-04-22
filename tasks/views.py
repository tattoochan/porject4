from django.shortcuts import render, redirect, get_object_or_404
from tasks.models import Job_detail
from tasks.forms import Job_form
from hands.views import profile
from django.contrib.auth.decorators import login_required

# Create your views here.
""" Show full job listing for applicant to apply """
def job_listing(request):
    result = Job_detail.objects.all()
    return render(request, 'job_listing.html',{
        'data':result
    })

""" Allow user to post a new job """    
@login_required
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
    
""" Allow user to edit the job listing """    
@login_required
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

@login_required
def delete_job(request,id):
    selected_job = get_object_or_404(Job_detail, pk=id)
    return render(request, 'delete_job.html',{
        'data': selected_job
    })
    
@login_required
def confirm_delete_job(request,id):
    Job_detail.objects.filter(pk=id).delete()
    return redirect(profile)
""" Allow user to delete the job listing """