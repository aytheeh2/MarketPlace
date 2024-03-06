from django.urls import path

from core.forms import LoginForm
from .import views
from django.contrib.auth.views import LoginView
app_name = 'core'
urlpatterns = [
    path('', views.home, name='home'),
    path('category/<str:name_of_category>/',
         views.ProductsInEachCategory, name='ProductsInEachCategory'),
    path('products/<int:pk>/', views.ProductDetails, name='ProductDetails'),
    path('register/', views.RegisterUser, name='register'),
    path('login/', views.Login_User, name='login'),
    path('logout/', views.Logout_User, name='logout'),
    path('add-item/', views.admin_add_item, name='admin_add_item'),
    path('edit-item/<int:pk>', views.admin_edit_item, name='admin_edit_item'),
    path('delete-item/<int:pk>', views.admin_delete_item, name='admin_delete_item'),
    path('search', views.search, name='search'),
]
