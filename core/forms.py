from django import forms
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Customer, Order, Product, Company, Supplier

# User Registration Form
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

# Customer Details Form
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['phone', 'address']

# Order Form
from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    PAYMENT_METHOD_CHOICES = [
        ('COD', 'Cash on Delivery'),
    ]

    payment_method = forms.ChoiceField(
        choices=PAYMENT_METHOD_CHOICES, widget=forms.RadioSelect, initial='COD'
    )

    class Meta:
        model = Order
        fields = ['product', 'quantity']


# Company Form
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'address', 'website', 'logo']

# Supplier Form
class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'email', 'phone', 'address', 'company']

# Product Form
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'quantity', 'supplier', 'company']
