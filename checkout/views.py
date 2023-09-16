import os

from django.contrib import messages
from django.shortcuts import redirect, render, reverse

from .forms import OrderForm


def checkout(request):

    stripe_public_key = os.environ.get('STRIPE_PUBLIC_KEY')
    client_secret = os.environ.get('CLIENT_SECRET')

    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': client_secret,
    }

    return render(request, template, context)
