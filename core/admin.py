from django.contrib import admin
from .models import Company, Supplier, Product, Customer, Payment, Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'product', 'quantity', 'status', 'date_ordered')
    list_filter = ('status', 'date_ordered')
    search_fields = ('customer__user__username', 'product__name')

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'website')

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'company')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'sold_quantity', 'supplier', 'company')

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'customer', 'amount', 'date', 'payment_method', 'status')
    list_filter = ('status', 'payment_method')
    search_fields = ('customer__user__username', 'order__id')
