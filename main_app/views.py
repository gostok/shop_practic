from django.shortcuts import render
from goods_app.models import *


def index(request):
    categories = Categories.objects.all()
    context = {
        "title": "Home - Главная",
        "content": "Магазин мебели HOME",
        "categories": categories,
    }
    return render(request, "index.html", context)


def about(request):
    context = {
        "title": "Home - О нас",
        "content": "О нас",
        "text_on_page": "Текст о нас и о магазине.",
    }
    return render(request, "about.html", context)
