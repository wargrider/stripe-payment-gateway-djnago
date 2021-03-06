from django.shortcuts import render
from stripe_payment.settings import STRIPE_PUBLISHABLE_KEY, STRIPE_SECRET_KEY
import stripe


stripe.api_key = STRIPE_SECRET_KEY

# Create your views here.


def index(request):
    return render(request, 'home.html', {'arr':[5.0,10.0,15.0,20.0]})


def payment(request):
    if request.method == 'POST':
        context = {'key': STRIPE_PUBLISHABLE_KEY, 'amount': request.POST['amount']}
        return render(request, 'payment.html', context)


def charge(request):
    if request.method == 'POST':
        amount = int(float(request.POST['amount']))
        charge = stripe.Charge.create(
            amount=amount,
            currency='usd',
            description='A Django charge',
            source=request.POST['stripeToken']
        )
        return render(request, 'charge.html', {'amount': amount/100})
