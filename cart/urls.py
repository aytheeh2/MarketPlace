from django.urls import path
from .import views

app_name = 'cart'
urlpatterns = [
    path('', views.view_cart, name='view_cart'),
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('substract-from-cart/<int:pk>/',views.substract_from_cart, name='substract_from_cart'),
    path('delete-from-cart/<int:pk>/',views.delete_from_cart, name='delete_from_cart'),
    path('checkout', views.checkout, name='checkout'),
]
