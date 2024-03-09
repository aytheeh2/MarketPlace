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



    # cart/order/checkout/success/1198/
]
