from django.shortcuts import render, redirect
from .import models
from Products.models import Category, Item, Offers
from .models import Cart
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


@login_required
def add_to_cart(request, pk):
    product = Item.objects.get(pk=pk)
    user = request.user
    try:
        cart = Cart.objects.get(user=user, products=product)
        if cart.quantity < cart.products.stock:
            cart.quantity += 1
            messages.success(request, f'Product {product.name} added to cart!')
            # product.stock -= 1 #commenting becasue its still only in users cart and user hasnt confirmed or received the product
            cart.save()
            # Bug : When adding item to cart, redirects to cart page, if not redirected,gets "httperroer did not return httpobject"
            return redirect('cart:view_cart')
            # return JsonResponse({'success': True})
    except Cart.DoesNotExist:
        if product.stock > 0:
            cart = Cart.objects.create(user=user, products=product, quantity=1)
            # product.stock -= 1 #commenting becasue its still only in users cart and user hasnt confirmed or received the product
            cart.save()
        messages.success(request, f'Product {product.name} added to cart!')
        # Bug : When adding item to cart, redirects to cart page, if not redirected,gets "httperroer did not return httpobject"
        return redirect('cart:view_cart')
        # return JsonResponse({'success': True})
    messages.success(
        request, f'Sorry! Maximum cart value for {product.name} has exceeded!')
    # return JsonResponse({'success': False})
    # Bug : When adding item to cart, redirects to cart page, if not redirected,gets "httperroer did not return httpobject"
    return redirect('cart:view_cart')


@login_required
def substract_from_cart(request, pk):
    product = Item.objects.get(pk=pk)
    user = request.user
    try:
        cart = Cart.objects.get(user=user, products=product)
        if cart.quantity > 1:
            cart.quantity -= 1
            cart.save()
            messages.success(
                request, f"Product {product.name} has been removed to the cart!")
        else:
            cart.delete()
            messages.success(
                request, f"Product {product.name} has been removed to the cart!")
    except:
        pass
    return redirect('cart:view_cart')


def view_cart(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)

    # Fetch the latest offer for each product in the cart and calculate subtotal
    total_amount = 0
    for cart_item in cart_items:
        if cart_item.products.offers.exists():
            cart_item.latest_offer = cart_item.products.offers.latest(
                'offer_date_added')
            subtotal = cart_item.latest_offer.offer_discount * cart_item.quantity
        else:
            subtotal = cart_item.subtotal()
        total_amount += subtotal
        cart_item.subtotal_amount = subtotal

    return render(request, 'cart.html', {'cart_items': cart_items, 'total_amount': total_amount})


@login_required
def delete_from_cart(request, pk):
    user = request.user
    product = Item.objects.get(pk=pk)
    try:
        cart = Cart.objects.filter(user=user, products=product)
        cart.delete()
        messages.success(
            request, f'The Product {product.name} has been deleted from cart!')
        return redirect('cart:view_cart')
    except:
        pass
    return redirect('cart:view_cart')


@login_required
def checkout(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)

    # Fetch the latest offer for each product in the cart and calculate subtotal
    total_amount = 0
    for cart_item in cart_items:
        if cart_item.products.offers.exists():
            cart_item.latest_offer = cart_item.products.offers.latest(
                'offer_date_added')
            subtotal = cart_item.latest_offer.offer_discount * cart_item.quantity
        else:
            subtotal = cart_item.subtotal()
        total_amount += subtotal
        cart_item.subtotal_amount = subtotal

    return render(request, 'order_form.html', {'cart_items': cart_items, 'total_amount': total_amount})
