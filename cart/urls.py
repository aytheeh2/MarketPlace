from django.urls import path, include
from .import views

app_name = 'cart'
urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('substract-from-cart/<int:pk>/',
         views.substract_from_cart, name='substract_from_cart'),
    path('delete-from-cart/<int:pk>/',
         views.delete_from_cart, name='delete_from_cart'),
    path('order/', views.place_order_form, name='order_view'),
    path('order/checkout/', views.checkout, name='checkout'),
    path('order/checkout/success/<int:total_amount>/',
         views.payment_success, name='payment_success'),
    path('order/checkout/failed/<int:total_amount>/',
         views.payment_failed, name='payment_failed'),
    path('delete_cart_after_payment_success', views.delete_cart_after_payment_success,
         name='delete_cart_after_payment_success'),




    path('set_order_completed/', views.set_order_completed,
         name='set_order_completed'),
]
