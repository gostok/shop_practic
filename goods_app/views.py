from unicodedata import category
from django.shortcuts import get_object_or_404, render

from goods_app.models import Categories, Products


def catalog(request, category_slug):
    if category_slug == "all":
        goods = Products.objects.all()
    else:
        goods = get_object_or_404(Products.objects.filter(category__slug=category_slug))

    context = {
        "title": "Home - Каталог",
        "goods": goods,
    }
    return render(request, "catalog.html", context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {
        "product": product,
    }
    return render(request, "product.html", context)
