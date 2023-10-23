from django .contrib .auth .models import User
from django .contrib .auth .forms import UserCreationForm
from .models import contact,Order
from django import forms

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=20)
    Phone_no = forms.CharField(max_length=20)
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','Phone_no','email']

class contactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = '__all__'

class orderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'