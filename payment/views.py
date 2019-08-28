from django.shortcuts import render
from stripe_payment.settings import STRIPE_PUBLISHABLE_KEY, STRIPE_SECRET_KEY
import stripe


stripe.api_key = STRIPE_SECRET_KEY

# Create your views here.


def index(request):
    return render(request, 'home.html', {'arr':[5,10,15,20]})


def payment(request):
    if request.method == 'POST':
        breakpoint()
        context = {'key': STRIPE_PUBLISHABLE_KEY}
        return render(request, 'payment.html', context)


def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='usd',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
        return render(request, 'charge.html')
