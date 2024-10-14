from django.shortcuts import render


def index(request):
    context = {"title": "Home", "content": "Главная страница магазина - HOME"}
    return render(request, "index.html", context)


def about(request):
    return render(request, "index.html")
