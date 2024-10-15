from django.shortcuts import render


def catalog(request):
    return render(request, "catalog.html")


def product(request):
    return render(request, "product.html")
