import stripe 
from django.shortcuts import render, redirect, reverse, get_object_or_404
from hands.models import Hands_info
from hands.views import help_list
from django.conf import settings
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def booking(request, id):
    selected_profile = get_object_or_404(Hands_info, pk=id)
    amount = selected_profile.rate_per_day * 100
    # return render(request, "booking.html", {
    #     'data' : selected_profile
    # })
    
    if request.method == 'GET':
        key = settings.STRIPE_PUBLISHABLE_KEY #1
        return render(request, 'booking.html', {
            'key' : key,
            'amount' : amount,
            'data' : selected_profile,
        })
    else:
        stripe.api_key = settings.STRIPE_SECRET_KEY #2
        charge = stripe.Charge.create(
            amount= amount,
            currency='sgd',
            description='2nd charge',
            source=request.POST['stripeToken']
        )
        return redirect(reverse('help_list'))