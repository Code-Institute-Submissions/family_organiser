from django.shortcuts import render
from django.conf import settings

import stripe

# Create your views here.
def premium_info(request):
    """
    View the benefits of purchasing a premium account.
    """
    return render(request, 'premium/premium_info.html')

def make_payment(request):
    """
    The form for processing the payment and sending the form to stripe.
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe_total = 199
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    if not stripe_public_key:
        print('Stripe public key is missing. Did you forget to set it in your environment?')

    context = {
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, 'premium/make_payment.html' ,context)