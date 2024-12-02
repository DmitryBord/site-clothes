from django.shortcuts import render


# Create your views here.
def orders(request):
    context = {
        "title": "Store - Заказы"
    }
    return render(request, "orders/orders.html", context)
