from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import contact, Order
from .forms import contactForm , orderForm
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.conf import settings
import stripe


# home
def home(request):
    return render(request, 'home.html')


# login
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        User = authenticate(request, username=username, password=password)
        if User is not None:
            login(request, User)
            return redirect('home')
        else:
            messages.info(request, 'Logged in Successfully')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# signup
def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
        return redirect('signup')
    else:
        messages.info(request, 'Register Successful')
        form = UserRegisterForm()
    return render(request, 'signup.html', {'form': form})


# view
def view(request):
    return render(request, 'gta.html')


# checkout
def checkout(request):
    if request.method == 'POST':
        form = orderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('payment')
    else:
        form =orderForm()
    return render(request, 'order.html', {'form': form})



# Payment Stripe
class payment(TemplateView):
    template_name = 'payment.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.STRIPE_PUBLISHABLE_KEY
        return context


def charge(request):
    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=500,
            currency='inr',
            description='Payment Gateway',
            source=request.POST['stripeToken']
        )
        return render(request, 'charge.html')


def charge(request):
    return render(request, 'charge.html')


# feedback
def feedback(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Thanks for Contacting Us')
            return redirect('home')
    else:
        form = contactForm
    return render(request, 'contact.html', {'form': form})
