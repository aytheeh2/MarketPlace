from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm, ItemForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.views.generic import ListView
from Products.models import Category, Item, Offers
from django.contrib.auth.decorators import login_required


# class Home(ListView):
#     queryset = Category.objects.all()
#     context_object_name = 'categories'
#     template_name = 'index.html'

def home(request):
    categories = Category.objects.all()
    products = Item.objects.all().order_by(
        '-created_at')[:3]  # latest prod section in index.html
    offer_products = Offers.objects.all().order_by('-offer_date_added')

    return render(request, 'index.html', {
        'categories': categories,
        'products': products,
        'offer_products': offer_products,
    })


def ProductsInEachCategory(request, name_of_category):
    category = Category.objects.get(name=name_of_category)
    categories = Category.objects.all().exclude(name=category.name).order_by('?')
    products = Item.objects.filter(category=category)
    return render(request, 'ProductsInEachCategory.html', {
        'products': products,
        'category': category,
        'categories': categories,
    })


def ProductDetails(request, pk):
    product = get_object_or_404(Item, pk=pk)
    # try:
    #     related_products = Item.objects.filter(
    #         category=product.category).exclude(pk=product.id)
    # except Item.DoesNotExist:
    #     pass

    related_products = Item.objects.filter(
        category=product.category).exclude(pk=product.id)

    other_categories = Category.objects.all().exclude(
        name=product.category).order_by('?')[:3]

    return render(request, 'ProductDetails.html', {
        'product': product,
        'related_products': related_products,
        'other_categories': other_categories,
    })


def search(request):
    search_results = []
    querry = ""
    if request.method == "GET":
        querry = request.GET['q']
        if querry:
            search_items = (Item.objects.filter(Q(name__icontains=querry) | Q(
                description__icontains=querry) | Q(price__icontains=querry)))

            search_category = (
                Category.objects.filter(Q(name__icontains=querry)))

            search_results.extend(search_items)
            search_results.extend(search_category)
            print(*search_results)
            return render(request, 'search_results.html', {
                'querry': querry,
                'search_results': search_results,
            })

    else:
        search_items = ""
        querry = ""


def RegisterUser(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Registration Successful, Happy Shopping")
            return redirect('core:home')
        else:
            messages.success(request, "Registration failed, Try again!")
    else:
        form = RegisterForm()
    return render(request, 'Register.html', {
        'form': form
    })


def Login_User(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, f'Login Success, Welcome {username}')
            return redirect('core:home')
        else:
            messages.success(request, 'Inavalid Credentials')
    form = LoginForm()
    return render(request, 'login.html', {
        'form': form,
    })


@login_required
def Logout_User(request):
    logout(request)
    messages.success(request, "Logged out")
    return redirect('core:home')


@login_required
def admin_add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.created_by = request.user
            new_item.save()
            messages.success(request, 'The Product has been added!')
            return redirect('core:home')
    form = ItemForm()
    return render(request, 'admin_add_item.html', {
        'form': form,
    })


@login_required
def admin_edit_item(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if request.method == "POST":
        item = ItemForm(request.POST, request.FILES, instance=item)
        if item.is_valid():
            item.save()
            messages.success(
                request, f"Product {request.POST['name']} Updated!")
            return redirect('core:home')
        else:
            messages.success(
                request, f"Updating {request.POST['name']} failed!")
    else:
        form = ItemForm(instance=item)
    return render(request, 'admin_edit_item.html', {
        'form': form,
    })


@login_required
def admin_delete_item(request, pk):
    if request.method == "POST":
        item = get_object_or_404(Item, pk=pk)
        if item:
            item.delete()
            messages.success(request, 'The item has been deleted!')
            return redirect('core:home')
    return render(request, 'delete_confirm.html')


def add_to_cart(request,pk):
    item=get_object_or_404(Item,pk=pk)
