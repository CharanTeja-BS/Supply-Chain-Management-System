from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Auth
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Orders
    path('order/', views.order_product, name='order_product'),
    path('my-orders/', views.my_orders, name='my_orders'),
    path('cancel-order/<int:order_id>/', views.cancel_order, name='cancel_order'),

    # Manage (Admin Only)
    path('manage/add-company/', views.add_company, name='add_company'),
    path('manage/add-supplier/', views.add_supplier, name='add_supplier'),
    path('manage/add-product/', views.add_product, name='add_product'),
    path('manage/orders/', views.view_orders, name='view_orders'),
] 
