# models.py
from django.db import models
from django.contrib.auth.models import User

# Company Module
class Company(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)

    def __str__(self):
        return self.name

# Supplier Module
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Product Module
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    sold_quantity = models.PositiveIntegerField(default=0)  # ✅ Add this line
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Customer Module
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.user.username

# Order Module

from django.utils import timezone 
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date_ordered = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered')
    ], default='Pending')

    def __str__(self):
        return f"Order #{self.id} - {self.customer.user.username}"

# Payment Module
class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=20, choices=[
        ('COD', 'Cash on Delivery'),
    ])
    status = models.CharField(max_length=20, choices=[
        ('Pending', 'Pending'),
        ('Completed', 'Completed')
    ], default='Pending')

    def __str__(self):
        return f"{self.customer.user.username} - ₹{self.amount}"
