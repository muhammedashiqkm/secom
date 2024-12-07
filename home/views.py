from django.shortcuts import render
from .models import Books

def home(request):
    books = Books.objects.all()
    return render(request, 'home.html', {'books': books})

def cart(request):
    # Example cart data
    cart_items = [
        {'name': 'Example Book', 'quantity': 2, 'total_price': 30.00},
    ]
    return render(request, 'cart.html', {'cart_items': cart_items})
