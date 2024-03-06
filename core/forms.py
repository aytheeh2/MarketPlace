from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from Products.models import Item, Category


# assigned to variable to avoid repetition , its only html class attributes
form_field_class = "form-control w-75 my-2 p-2 border shadow-sm"


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': "Username",
        'class': form_field_class,
    }))

    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'email',
        'class': form_field_class,
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': form_field_class,
    }))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class': form_field_class,
    }))


class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password',)

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': form_field_class,
    }))

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': form_field_class,
    }))


# html class for form fields
Item_field_classes = 'form-control my-2 p-2 border shadow-sm'


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        exclude = ('created_at', 'created_by',)

        widgets = {
            'category': forms.Select(attrs={
                'class': Item_field_classes,

            }),

            'name': forms.TextInput(attrs={
                'placeholder': 'Product Name',
                'class': Item_field_classes,
            }),

            'price': forms.TextInput(attrs={
                'class': Item_field_classes,
                'placeholder': 'Price',
            }),

            'description': forms.Textarea(attrs={
                'class': Item_field_classes,
                'placeholder': 'Description',
            }),

            'image': forms.FileInput(attrs={
                'class': Item_field_classes,
            }),

            'stock': forms.NumberInput(attrs={
                'class': Item_field_classes,
                'placeholder': 'Stock in number'
            })

        }
