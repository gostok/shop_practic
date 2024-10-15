from django.shortcuts import render

from goods_app.models import Products


def catalog(request):
    goods = Products.objects.all()
    context = {
        "title": "Home - Каталог",
        "goods": goods,
    }
    return render(request, "catalog.html", context)


def product(request):
    return render(request, "product.html")
