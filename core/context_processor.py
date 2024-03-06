from Products.models import Category, Item
from cart.models import Cart


def categories_context_function(request):
    all_categories = Category.objects.all()
    return {'category_context': all_categories}


def no_of_items_in_cart_context_function(request):
    no_of_items_in_cart = 0
    user = request.user
    try:
        cart_of_user = Cart.objects.filter(user=user)
        for i in cart_of_user:
            no_of_items_in_cart += i.quantity
    except:
        count = 0
    return {'no_of_items_in_cart_context': no_of_items_in_cart}
