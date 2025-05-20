from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import (
    UserRegistrationForm, CustomerForm,
    OrderForm, CompanyForm, SupplierForm, ProductForm
)
from .models import Product, Payment, Customer, Order, Company, Supplier

# Helper: Check if user is admin


def is_admin(user):
    return user.is_staff

# Home Page


def home(request):
    return render(request, 'home.html')

# User Registration


def register(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        customer_form = CustomerForm(request.POST)
        if user_form.is_valid() and customer_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            customer = customer_form.save(commit=False)
            customer.user = user
            customer.save()
            return redirect('login')
    else:
        user_form = UserRegistrationForm()
        customer_form = CustomerForm()
    return render(request, 'register.html', {
        'user_form': user_form,
        'customer_form': customer_form
    })

# Login View


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

# Logout


def logout_view(request):
    logout(request)
    return redirect('home')

# Dashboard


@login_required
def dashboard(request):
    products = Product.objects.all()
    orders = Order.objects.all() if request.user.is_staff else Order.objects.filter(
        customer__user=request.user)
    return render(request, 'dashboard.html', {
        'products': products,
        'orders': orders
    })

# Place an Order


@login_required
def order_product(request):
    customer = get_object_or_404(Customer, user=request.user)

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.customer = customer
            available_quantity = order.product.quantity - order.product.sold_quantity

            if order.quantity > available_quantity:
                messages.error(request, 'Not enough stock available.')
                return redirect('order_product')

            order.save()
            order.product.sold_quantity += order.quantity
            order.product.save()

    # ✅ This saves the payment entry
            Payment.objects.create(
                order=order,
                customer=customer,
                amount=order.quantity * order.product.price,
                payment_method='COD',  # <- ✅ Hardcoded unless you pass from form
                status='Pending',
            )

            messages.success(request, 'Order placed successfully!')
            return redirect('my_orders')

    else:
        form = OrderForm()

    products = Product.objects.all()
    return render(request, 'order_product.html', {'form': form, 'products': products})

# My Orders (Customer)


@login_required
def my_orders(request):
    customer = get_object_or_404(Customer, user=request.user)
    orders = Order.objects.filter(customer=customer).order_by('-date_ordered')
    return render(request, 'my_orders.html', {'orders': orders})

# Cancel Order


@login_required
def cancel_order(request, order_id):
    customer = get_object_or_404(Customer, user=request.user)
    order = get_object_or_404(Order, id=order_id, customer=customer)
    if order.status != 'Cancelled':
        order.status = 'Cancelled'
        order.save()

        order.product.quantity += order.quantity
        order.product.sold_quantity -= order.quantity
        order.product.save()

        payment = Payment.objects.filter(order=order).first()
        if payment:
            payment.status = 'Refunded'
            payment.save()

        messages.success(request, 'Order cancelled and refunded successfully.')
    else:
        messages.info(request, 'Order was already cancelled.')
    return redirect('my_orders')

# ===================== Admin Views =====================

# Add Company


@login_required
@user_passes_test(is_admin)
def add_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CompanyForm()
    return render(request, 'admin/add_company.html', {'form': form})

# Add Supplier


@login_required
@user_passes_test(is_admin)
def add_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = SupplierForm()
    return render(request, 'admin/add_supplier.html', {'form': form})

# Add Product


@login_required
@user_passes_test(is_admin)
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProductForm()
    return render(request, 'admin/add_product.html', {'form': form})

# View All Orders (Admin)


@login_required
@user_passes_test(is_admin)
def view_orders(request):
    orders = Order.objects.all().order_by('-date_ordered')
    return render(request, 'admin/view_orders.html', {'orders': orders})
